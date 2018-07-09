import socket
import struct
import json
import os
import hashlib

DOWNLOAD_DIR=r'D:\python21\day8\ftp作业\download'

class FtpClient:
    def __init__(self,host,port):
        self.host=host
        self.port=port
        self.client=socket.socket()
        self.client.connect((self.host,self.port))

    def login(self):
        userinfo = []
        while True:
            username = input('请输入你的用户名:')
            userinfo.append(username)
            pwd = input('请输入你的密码：')
            # userinfo.append(pwd)
            hash_user = hashlib.md5(username.encode('utf-8'))
            hash_pwd = hash_user.update(pwd.encode('utf-8'))
            md5_pwd = hash_user.hexdigest()
            userinfo.append(md5_pwd)
            userinfo_byttes = bytes(json.dumps(userinfo), encoding='utf-8')  # 把列表转换成bytes
            while True:
                self.client.send(userinfo_byttes)
                ret = self.client.recv(1024).decode('utf-8')
                print(ret)
                if ret=='true':
                    client.command()
                else:
                    client.login()

                #
            self.client.close()

    def command(self):
        while True:
            data=input('>>: ').strip() #get a.txt
            if not data:continue
            params=data.split() #parmas=['get','a.txt']
            cmd=params[0] #cmd='get'
            if hasattr(self,cmd):
                func=getattr(self,cmd)
                func(params) #func(['get','a.txt'])

    def get(self,params):
        params_json=json.dumps(params)
        self.client.send(params_json.encode('utf-8'))

        # 1、先接收报头的长度
        headers_size = struct.unpack('i', self.client.recv(4))[0]

        # 2、再收报头
        headers_bytes = self.client.recv(headers_size)
        headers_json = headers_bytes.decode('utf-8')
        headers_dic = json.loads(headers_json)
        print('========>', headers_dic)
        filename = headers_dic['filename']
        filesize = headers_dic['filesize']
        filepath = os.path.join(DOWNLOAD_DIR, filename)

        # 3、再收真实的数据
        with open(filepath, 'wb') as f:
            recv_size = 0
            while recv_size < filesize:
                line = self.client.recv(1024)
                recv_size += len(line)
                f.write(line)
            print('===>下载成功')

if __name__ == '__main__':
    client=FtpClient('127.0.0.1',8080)
    client.login()