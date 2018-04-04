import socket

name = input("Enter Target: ")
result = socket.gethostbyname(name)
print('The Host Name is: ' + result)
