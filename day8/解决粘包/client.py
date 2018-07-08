import socket
import struct
sk=socket.socket()
sk.connect(('127.0.0.1',8090))
num=sk.recv(4) #先接受bytes的长度
num=struct.unpack('i',num)[0]#提取报文的长度
print(sk.recv(num).decode('utf-8'))
print(sk.recv(10))

sk.close()