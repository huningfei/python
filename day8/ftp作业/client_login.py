import hashlib
import configparser
import socket
import struct
import json
sk=socket.socket()
sk.connect(('127.0.0.1',8090))
userinfo=[]
while True:
    username=input('请输入你的用户名')
    userinfo.append(username)
    pwd=input('请输入你的密码：')
    userinfo.append(pwd)
    # hash_user = hashlib.md5(username.encode('utf-8'))
    # hash_pwd=hash_user.update(pwd.encode('utf-8'))
    # md5_pwd=hash_user.hexdigest()
    # userinfo.append(md5_pwd)
    userinfo_byttes = bytes(json.dumps(userinfo),encoding='utf-8')  # 把列表转换成bytes
    sk.send(userinfo_byttes)
    ret=sk.recv(1024).decode('utf-8')
    print(ret)
sk.close()


# def login():
#     #登录认证,用了动态加盐
#     print('\033[1;32m------ftp系统------\033[0m')
#     userinfo=[]
#     username=input('请输入用户名>>>:')
#     userinfo.append('username')
#     pwd=input('请输入密码>>>:')
#     hash_user=hashlib.md5(username.encode('utf-8'))
#     hash_pwd=hash_user.update(pwd.encode('utf-8'))
#     md5_pwd=hash_user.hexdigest()
#     userinfo.append(md5_pwd)
#     userinfo_byttes = bytes(json.dumps(userinfo), encoding='utf-8')  # 把列表转换成bytes
#     sk = socket.socket()
#     sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     sk.bind(('127.0.0.1', 8090))
#     sk.listen()
#     conn, addr = sk.accept()
#     conn.send(userinfo_byttes)
#     conn.close()
#     sk.close()



if __name__=='__main__':
    login()