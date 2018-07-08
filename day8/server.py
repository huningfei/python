import socket
sk=socket.socket()  #实例化一个对象
sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)#端口可以重用
sk.bind(('127.0.0.1',9100))
sk.listen()#监听
while True:
    conn,addr=sk.accept() #阻塞，三次握手完毕
    while True:
        inp=input('请输入你要发送的消息：')
        conn.send(inp.encode('utf-8'))
        if inp == 'q': break
        ret=conn.recv(1024).decode('utf-8')
        if ret == 'q': break
        print(ret)

    conn.close()
sk.close()