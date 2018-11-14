#!/usr/bin/env python
import socket
import subprocess
import sys
import os, sys
import re

remoteServer = open("hosts.txt", 'r')

for line in remoteServer:
    #remoteServerIP  = socket.gethostbyname(remoteServer)

    try:
        for port in range(1,1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(("192.168.1.5", port))
            if result == 0:
                print "Port {}: 	 Open".format(port)
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
