import socket
sk=socket.socket()
sk.connect(('127.0.0.1',9000))
print(sk.recv(1024))
print(sk.recv(1024))
sk.close()
