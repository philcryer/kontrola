import sys
import socket

class PortScanner:
    def __init__(self, ip, ports):
        self.ip = ip
        self.ports = ports

    def scan_tcp_port(self, port):
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.settimeout(0.3)
        yield connection.connect_ex((self.ip, port)), port
        connection.close()

    def scan_ports(self):
        for port in self.ports:
            yield from self.scan_tcp_port(port)

    def host_up(self):
        try:
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection.connect_ex((self.ip, 80))
            return True
        except socket.timeout:
            return True
        except socket.error:
            return False


def main(ip, ports=range(1, 65536)):
    scanner = PortScanner(ip, ports)
    if not scanner.host_up():
        print("Host is down")
        return

    for connection, port in scanner.scan_ports():
        connection = "UP" if connection == 0 else "DOWN"
        print(f"Port {port} is {connection}") # Log result

if __name__ == '__main__':
    if len(sys.argv) == 2:
        ip = sys.argv[1]
        main(ip)
