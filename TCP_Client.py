import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=65432
s.connect((socket.gethostname(),port))
message=s.recv(1024)
print(message.decode("utf-8"))      
s.close()