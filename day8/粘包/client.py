import socket
ip_port=('127.0.0.1',8080)
sk=socket.socket()
res=sk.connect(ip_port)
sk.send('hello'.encode('utf-8'))
sk.send('egg'.encode('utf-8'))
sk.close()
