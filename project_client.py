import socket

port = 9999
host = "127.0.0.1"

s=socket.socket()

s.connect((host,port))

while True:
    data=s.recv(1024)
    print(data.decode("utf-8"))
    ans=input()
    s.send(str.encode(ans))
    data=s.recv(1024)
    print(data.decode("utf-8"))
    if data.decode("utf-8")=="You won!! Game ended":
        break