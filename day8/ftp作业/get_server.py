import socket
import os
import json
import struct
import configparser

SHARE_DIR=r'D:\python21\day8\ftp作业\sharedir'
user_status = {
    'username': None,
    'status': False
}

class FtpServer:
    def __init__(self,host,port):
        self.host=host
        self.port=port
        self.server=socket.socket()
        self.server.bind((self.host,self.port))
        self.server.listen()


    def register_login(self):
        config = configparser.ConfigParser()
        config.read('userinfo')
        user = config.sections()
        while True:
            print('server start')
            self.conn, self.client_addr = self.server.accept()
            print(self.client_addr)

            while True:
                ret=json.loads(self.conn.recv(1024).decode('utf-8'))
                print(ret)
                username = ret[0]
                print(username)
                pwd = ret[1]
                print(pwd)
                for i in user:
                    if i == username and config[username]['md5_pwd'] == pwd:
                        self.conn.send('true'.encode('utf-8'))
                        user_status['status'] = True

                else:
                   self.conn.send('你输入的用户名或密码错误'.encode('utf-8'))
            self.conn.close()
        self.server.close()

    def run(self):
        print('server starting...')
        while True:
            self.conn,self.client_addr=self.server.accept()
            print(self.client_addr)
            while True:
                try:
                    data=self.conn.recv(1024)  #params_json.encode('utf-8')
                    if not data:break
                    params=json.loads(data.decode('utf-8')) #params=['get','a.txt']
                    cmd=params[0] #
                    if hasattr(self,cmd):
                        func=getattr(self,cmd) #对象
                        func(params)
                    else:
                        print('\033[45mcmd not exists\033[0m')
                except ConnectionResetError:
                    break
            self.conn.close()
        self.server.close()

    def get(self,params): #params=['get','a.txt']
        filename=params[1] #filename='a.txt'
        filepath=os.path.join(SHARE_DIR,filename) #
        if os.path.exists(filepath):
            #1、制作报头
            headers = {
                'filename': filename,
                'md5': '123sxd123x123',
                'filesize': os.path.getsize(filepath)
            }

            headers_json = json.dumps(headers)
            headers_bytes = headers_json.encode('utf-8')

            #2、先发报头的长度
            self.conn.send(struct.pack('i',len(headers_bytes)))

            #3、发送报头
            self.conn.send(headers_bytes)

            #4、发送真实的数据
            with open(filepath,'rb') as f:
                for line in f:
                    self.conn.send(line)

    def put(self):
        pass

if __name__ == '__main__':
    server=FtpServer('127.0.0.1',8080)
    server.register_login()

