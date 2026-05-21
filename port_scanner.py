import socket

services = {
    80: 'HTTP',
    443: 'HTTPS',
    22: 'SSH',
    21: 'FTP'
}

target = 'google.com'
ports = [80, 443, 22, 21]

open_port = 0
close_port = 0

print(f"\nScanning Target\n")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} Is Open - {services[port]}")
        open_port += 1
    else:
        print(f"Port {port} Is Closed")
        close_port += 1

    s.close()

print("------------------SCAN COMPLETED------------------")
print("OPEN PORTS: ", open_port)
print("CLOSE PORTS: ", close_port)