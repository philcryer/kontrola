#!/usr/bin/env python

def scanhosts():
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
        if ifaceName == "wlan0":
            return ', '.join(addresses)

 def scanlooper(subnet):
    for i in range(0,1):
        for x in range(0,999):
            s = "%s.%s.%s" % (subnet,i,x)
            request = urllib2.Request('http://%s/' % s)
            try:
                response = urllib2.urlopen(request)
                html = response.read()
                if html != "False":
                    print "%s is hosting a server" % s
            except:
                print "%s is not hosting a server" % s

localip = scanhosts()
ipstrip = localip.strip(".")
subnet = "%s.%s" % (ipstrip[0],ipstrip[1])
scanlooper(subnet)
