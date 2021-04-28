import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#print('success')
port=65432
s.bind((socket.gethostname(),port))
print(f"socket binded to {port}")
s.listen(5)
print(f"is listening..........")
while True:
	clientsocket,addr=s.accept()
	message='Welcome to my chat room!!!'
	print(f'connection recieved from {addr[0]} on the port {port}')
	clientsocket.send(bytes(message,"utf-8"))
	clientsocket.close()
	exit()