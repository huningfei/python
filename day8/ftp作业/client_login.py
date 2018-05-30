import hashlib
import configparser
import socket
import struct
import json

# def login(self):
#     sk=socket.socket()
#     sk.connect(('127.0.0.1',8090))
#     userinfo=[]
#     while True:
#         username=input('请输入你的用户名')
#         userinfo.append(username)
#         pwd=input('请输入你的密码：')
#         #userinfo.append(pwd)
#         hash_user = hashlib.md5(username.encode('utf-8'))
#         hash_pwd=hash_user.update(pwd.encode('utf-8'))
#         md5_pwd=hash_user.hexdigest()
#         userinfo.append(md5_pwd)
#         userinfo_byttes = bytes(json.dumps(userinfo),encoding='utf-8')  # 把列表转换成bytes
#         sk.send(userinfo_byttes)
#         ret=sk.recv(1024).decode('utf-8')
#         print(ret)
#
#     sk.close()

# if __name__=='__main__':
#     login()

class Client():
    def __init__(self,ip_port):
        self.ip_port=ip_port
    #@classmethod
    def init_sokcet(self):
        global sk
        sk = socket.socket()
        sk.connect((self.ip_port))
    def login(self):
        global sk
        userinfo = []
        while True:
            username=input('请输入你的用户名')
            userinfo.append(username)
            pwd=input('请输入你的密码：')
            #userinfo.append(pwd)
            hash_user = hashlib.md5(username.encode('utf-8'))
            hash_pwd=hash_user.update(pwd.encode('utf-8'))
            md5_pwd=hash_user.hexdigest()
            userinfo.append(md5_pwd)
            userinfo_byttes = bytes(json.dumps(userinfo),encoding='utf-8')  # 把列表转换成bytes
            while True:
                # sk=Client.init_sokcet()
                # sk.send(userinfo_byttes)
                sk.send(userinfo_byttes)
                ret=sk.recv(1024).decode('utf-8')
                print(ret)
            sk.close()

client=Client(('127.0.0.1',8090))
client.login()