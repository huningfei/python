import hashlib
import configparser
import socket
import struct
import json

def register_login():
    # global conn
    # global user_pwd
    # while True:
    config = configparser.ConfigParser()
    config.read('userinfo')
    user = (config.sections())
    for i in user:
        if i == username and  config[i]['passwd']== pwd:
            conn.send('登录成功'.encode('utf-8'))
        else:
            conn.send('你输入的用户名或密码错误'.encode('utf-8'))


sk=socket.socket()
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk.bind(('127.0.0.1', 8090))
sk.listen()
while True:
    conn,addr=sk.accept()
    print('连接成功')
    while True:
        user_pwd=json.loads(conn.recv(1024).decode('utf-8'))
        username=user_pwd[0]
        pwd=user_pwd[1]
        print(user_pwd[0],user_pwd[1])
        register_login()


    conn.close()
sk.close()

# def init_socker():
#     sk=socket.socket()
#     sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#     sk.bind(('127.0.0.1',8090))
#     sk.listen()
#     while True:
#         print('>>>等待客户端连接...')
#         conn,addr=sk.accept()
#         print('连接成功')
#         while True:
#             print('------等待接收')
#             ret=conn.recv(1024).decode('utf-8')#接受到一个字符串
#             user_pwd=json.load(ret)
#         conn.close()
#     sk.close()
#
#


if __name__=='__main__':
    #init_socker()
    register_login()
