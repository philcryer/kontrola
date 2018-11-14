#!/usr/bin/env python

import socket
import subprocess
import sys
from datetime import datetime

port_list = [22, 80, 443, 8443, 646]
time_stamp_start = datetime.now()

subprocess.call('clear', shell=True)

remoteServer    = 'lnxvmpccryerd01'
remoteServerIP  = socket.gethostbyname(remoteServer)

try:
    for port_number in port_list:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port_number))
        if result == 0:
            print "Port {}: 	 Open".format(port_number)
        sock.close()

except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()

time_stamp_stop = datetime.now()
total =  time_stamp_stop - time_stamp_start
print 'Scanning Completed in: ', total
