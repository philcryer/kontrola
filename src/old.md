https://github.com/Matty9191/ssl-cert-check


#!/usr/bin/env bash

expireDays="45"
emailAddress="phil@philcryer.com"
reportDay="$(date +%Y-%m-%d)"
reportDir="reports/${reportDay}"
http_proxy="http://10.0.0.250:80"
https_proxy="http://10.0.0.250:80"

preFlight () {
    echo "* Preflight checks"
    for cli in nmap openssl date; do
        if ! type "$cli" > /dev/null 2>&1; then
            echo "ERROR: $cli is not installed, or in the PATH. Aborting."
        fi
    done
    if [ ! -f 'hosts.txt' ]; then
        echo "ERROR file hosts.txt not found"
        exit 1
    fi
    if [ ! -f 'ports.txt' ]; then
        echo "ERROR file ports.txt not found"
        exit 1
    fi
}

buildList () {
    cat hosts.txt | sort -u > hosts.in
    cat ports.txt | sort -u > ports.in
    hostTotal=$(cat hosts.in | wc -l)
    portTotal=$(cat ports.in | wc -l)
    echo "* File hosts.check - building (${hostTotal} hosts, ${portTotal} ports)"
    cat hosts.in | while read hostName
    do
        cat ports.in | while read portNumber
        do
            checkPort
            echo -n " ."
            if [ "${checkPort_result}" -gt "0" ]; then
                echo "$hostName $portNumber" >> hosts.check
            fi
        done
    done
    echo
}

checkPort () {
    checkPort_result=$(nmap --open -pT${portNumber} ${hostName} | grep "/tcp open " | wc -l)
}

lookupCert () {
    lineTotal=$(cat hosts.check | wc -l)
    echo "* Querying certificates (${lineTotal} records)"
    cat hosts.check | while read hostToCheck
    do
        echo -n " ."
        echo -n "    * " >> hosts.out
        echo -n "$hostToCheck" >> hosts.out
        today=`date +%D`
        #expiredate=`echo | openssl s_client -servername ${hostName} -connect ${hostName}:443 2>/dev/null | openssl x509 -enddate -noout | awk -F'=' '{print $2}'`
        expiredate=`echo | openssl s_client -connect ${hostToCheck} 2>/dev/null | openssl x509 -enddate -noout | awk -F'=' '{print $2}'`
        expdate=`date +%D --date="$expiredate"`
        ed="$expdate"
        daysleft=`echo $(($(($(date -u -d "$ed" "+%s") - $(date -u -d "$today" "+%s"))) / 86400))`
        echo -n ",$daysleft" >> hosts.out
        echo ", certificate due on $expiredate" >> hosts.out
    done
    echo
}

buildReport () {
    if [ ! -d '${reportDir}' ]; then
        mkdir -p ${reportDir}
    fi
    cp hosts.out ${reportDir}/ssl-report.txt
    reportTotal=$(cat ${reportDir}/ssl-report.txt | wc -l)
    cp hosts.check ${reportDir}/ssl-hosts.txt
    echo "* Certificate report complete (${reportTotal} entries)"
}

buildSummary () {
    echo "* Summary"
        total443=$(cat ${reportDir}/ssl-report.txt | grep :443 |  wc -l)
        total8443=$(cat ${reportDir}/ssl-report.txt | grep :8443 | wc -l)
        total636=$(cat ${reportDir}/ssl-report.txt | grep :636 | wc -l)

        echo " - Port 443:      ${total443}"
        echo " - Port 8443:     ${total8443}"
        echo " - Port 636:      ${total636}"
        echo " -----------------------------"
        echo "   All            ${reportTotal}"
        echo "   Expiring in less than ${expireDays} days: $(cat ${reportDir}/ssl-expiring-in-less-than-${expireDays}.txt | wc -l)"

        echo " ALL SCANNED SSL HOSTS" > ${reportDir}/ssl-summary.txt
        echo " -----------------------------" >> ${reportDir}/ssl-summary.txt
        echo " - Port 443:      ${total443}" >> ${reportDir}/ssl-summary.txt
        echo " - Port 8443:     ${total8443}" >> ${reportDir}/ssl-summary.txt
        echo " - Port 636:      ${total636}" >> ${reportDir}/ssl-summary.txt
        echo " -----------------------------" >> ${reportDir}/ssl-summary.txt
        echo "   All            ${reportTotal}" >> ${reportDir}/ssl-summary.txt
        echo "   Expiring in less than ${expireDays} days: $(cat ${reportDir}/ssl-expiring-in-less-than-${expireDays}.txt | wc -l)" >> ${reportDir}/ssl-summary.txt
}

sortDays () {
    echo "* Looking for certs expiring in less than ${expireDays} days"
    cat ${reportDir}/ssl-report.txt | while read hostPortDaysLine
    do
        daysUntilDue=$(echo ${hostPortDaysLine} | cut -d',' -f2)
        #echo "${daysUntilDue}"; echo "${expireDays}"
        if [ "${daysUntilDue}" -lt "${expireDays}" ]; then
           echo "${hostPortDaysLine}" >> ${reportDir}/ssl-expiring-in-less-than-${expireDays}.txt
        fi
    done
    echo
    cp ${reportDir}/ssl-expiring-in-less-than-${expireDays}.txt ${reportDir}/ssl-$(cat ${reportDir}/ssl-expiring-in-less-than-${expireDays}.txt | wc -l)-certs-expiring-in-less-than-${expireDays}.txt
    cp ${reportDir}/ssl-expiring-in-less-than-${expireDays}.txt ${reportDir}/ssl-$(cat ${reportDir}/ssl-expiring-in-less-than-${expireDays}.txt | wc -l)-certs-expiring-in-less-than-${expireDays}.txt
    cp ${reportDir}/ssl-$(cat ${reportDir}/ssl-expiring-in-less-than-${expireDays}.txt | wc -l)-certs-expiring-in-less-than-${expireDays}.txt ${reportDir}/email.txt
}

mailSummary () {
    echo "* Emailing summary"
    emailSubject="[$(cat ${reportDir}/email.txt | wc -l)] SSL certs expiring in less than ${expireDays} days"
    emailTo="${emailAddress}"
    emailMessage="${reportDir}/email.txt"
    /usr/bin/mail -s "${emailSubject}" "${emailTo}" < "${emailMessage}"
}

cleanUp () {
    echo "* Cleanup"
    rm -f hosts.in hosts.out hosts.check
}

preFlight

if [ ! -f 'hosts.check' ]; then
    buildList
else
    echo "* File hosts.check - exists"
fi

#lookupCert
#buildReport
#sortDays
#buildSummary
#mailSummary
#cleanUp

exit 0
