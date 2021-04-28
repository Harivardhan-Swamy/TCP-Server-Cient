import socket
HEADERSIZE = 10

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=65431
#s.bind((socket.gethostname(),port))
s.connect((socket.gethostname(),port))


while True:
    full_msg=''
    new_msg=True


    while True:
        msg=s.recv(16)

        if new_msg:
            print(f"new message length is {msg[:HEADERSIZE]}")
            msglen=int(msg[:HEADERSIZE])
            new_msg=False

        print(f"fullmsg len {msglen}")
        full_msg+=msg.decode("utf-8")
        print(len(full_msg))

        if len(full_msg)-HEADERSIZE == msglen:
            print("ful msg recvd")
            print(full_msg[HEADERSIZE:])
            new_msg=True
            full_msg=''
    
    print(full_msg)