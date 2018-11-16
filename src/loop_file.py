#!/usr/bin/env python
# -*- coding: ascii -*-
import os, sys
import socket
import subprocess
import sys
from datetime import datetime

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
