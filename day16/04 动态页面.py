import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()


# 定义一个专门用来处理访问index的函数
def index():
    with open('index.html', 'r', encoding='utf8') as f:
        data = f.read()
    import time
    now = str(time.time())
    data_s = data.replace('@@XX@@', now)
    return bytes(data_s, encoding='utf8')


def home():
    return b'home'


# 定义一个访问路径和将要执行的函数的对应关系
url_func = [
    ('/index/', index),
    ('/home/', home),
]

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
    for i in url_func:
        if i[0] == url:
            func = i[1]
            break
    else:
        func = None
    if func:
        msg = func()
    else:
        msg = b'404 not found!'

    # 回复消息
    # 按照约定好的格式回复消息
    conn.send(b'http/1.1 200 ok\r\n\r\n')
    conn.send(msg)
    conn.close()
