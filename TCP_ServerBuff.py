import socket

HEADERSIZE = 10

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=65431
s.bind((socket.gethostname(),port))
s.listen(5)

while True:
    clientsocket,addr=s.accept()
    print(f'connection has been established from {addr[0]} at port {port}')
    msg = 'Welcome to the server!'
    msg = f'{len(msg):<{HEADERSIZE}}' + msg
    clientsocket.send(bytes(msg,"utf-8"))



