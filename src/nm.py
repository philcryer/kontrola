import nmap
import optparse

def main():
    parser = optparse.OptionParser('-H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target port[s] separated by comma')
    (options, args) = parser.parse_args()
    if not options.tgtHost or not options.tgtPort:
        print parser.usage
        exit(0)
    tgtHost = options.tgtHost
    tgtPorts = options.tgtPort

    nm = nmap.PortScanner()
    res = nm.scan(tgtHost,tgtPorts)
    for port in nm[tgtHost]["tcp"].keys():
        print "[*]  {} tcp/{} {}".format(tgtHost,port,res["scan"][tgtHost]["tcp"][int(port)]["state"])

if __name__ == '__main__':
    main()
