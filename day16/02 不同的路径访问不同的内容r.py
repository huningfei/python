import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()


while 1:
    conn, addr = sk.accept()
    # 接收消息
    data = conn.recv(8000)
    # print(data)
    # 把字节类型的数据转换成字符串
    data_str = str(data, encoding="utf8")
    # 将收到的消息按照\r\n分割,得到第一行
    first_line = data_str.split("\r\n")[0]
    # 对第一行按照空格分
    url = first_line.split()[1]
    print(url)
    # 根据用户访问的路径返回不同的内容
    if url == "/index/":
        msg = b'index'
    elif url == "/home/":
        msg = b'home'
    else:
        msg = b'404 not found'
    # 回复消息
    # 按照约定好的格式回复消息
    conn.send(b'http/1.1 200 ok\r\n\r\n')
    conn.send(msg)
    conn.close()


