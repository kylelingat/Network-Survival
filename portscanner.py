import socket
import sys

target    = input("Target: ")
targetIP  = socket.gethostbyname(target)

try:
    for port in range(1,1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((targetIP, port))
        if result == 0:
            print("Port {}: 	 Open".format(port))

except socket.error:
    sys.exit()

except KeyboardInterrupt:
    sys.exit()
