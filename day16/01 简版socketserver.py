import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()


while 1:
    conn, addr = sk.accept()
    # 接收消息
    data = conn.recv(8000)
    print(data)
    # 回复消息
    # 按照约定好的格式回复消息
    conn.send(b'http/1.1 200 ok\r\n\r\no98k')
    conn.close()


