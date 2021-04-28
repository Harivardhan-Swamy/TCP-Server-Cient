#!usr/bin/python3

import socket
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='192.168.56.1'
port=65432
clientsocket.connect((host,port))
message=clientsocket.recv(1024)
clientsocket.close()
print(message.decode('ascii'))
