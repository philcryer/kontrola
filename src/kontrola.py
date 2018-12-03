<<<<<<< HEAD
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
||||||| merged common ancestors
=======
#!/usr/bin/env python

import socket
import subprocess
import sys
from datetime import datetime

port_list = [22, 80, 443, 8443, 646]
time_stamp_start = datetime.now()
subprocess.call('clear')

# https://stackoverflow.com/questions/3277503/in-python-how-do-i-read-a-file-line-by-line-into-a-list

with open('hosts.txt', 'r') as host_name:
    for line in host_name:
        #remoteServer = 'cnn.com'
        #remoteServerIP  = socket.gethostbyname(remoteServer)
        #remoteServerIP  = '192.168.1.5'

        try:
            for port_number in port_list:
                remoteServer = host_name.read()
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                #result = sock.connect_ex((remoteServerIP, port_number))
                result = sock.connect_ex((remoteServer, port_number))
                if result == 0:
                    #print "Host {}:      ".format(remoteServerIP)
                    #print format(remoteServerIP),format(port_number)
                    print format(remoteServer),format(port_number)
                    #print "Port {}: 	 Open".format(port_number)
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
>>>>>>> d13cbc05b61bb4ec7d60f1bc017c6891c9fa5bbd
