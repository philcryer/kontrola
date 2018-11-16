#!/usr/bin/env python
import os
import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear', shell=True)

remoteServer    = '127.0.0.1'
remoteServerIP  = socket.gethostbyname(remoteServer)

print "-" * 60
print "Please wait, scanning remote host", remoteServerIP
print "-" * 60

t1 = datetime.now()

# Using the range function to specify ports (here it will scans all ports between 1 and 1024)
port_list = [22, 80, 443, 8443, 646]

#for port_number in port_list:
#    print port_number

# We also put in some error handling for catching errors

try:
    #to scan a range:
    #for port in range(1,1025):
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

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print 'Scanning Completed in: ', total




#!/usr/bin/env python
# -*- coding: ascii -*-
import socket
import subprocess

subprocess.call('clear', shell=True)

with open("hosts.txt", 'r') as remoteServer:
    for line in remoteServer:
        try:
            for port in range(1,1025):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((remoteServer, port))
            if result == 0:
                print "Port {}: 	 Open".format(port)
            sock.close()
