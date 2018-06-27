import socket
sk=socket.socket()
sk.bind(('127.0.0.1',8000))
sk.listen()
while True:
    print('启动服务端....')
    conn,addr=sk.accept()
    ret=conn.recv(1024)
    res=ret.decode('gbk')
    print(res)
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    conn.send('注册成功'.encode('gbk'))
    conn.close()