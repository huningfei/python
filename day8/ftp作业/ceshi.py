import socket
import json
import configparser
class Server:
    def __init__(self,ip_port):
        self.ip_port=ip_port
    def init_socket(self):

        global conn
        global ret
        sk = socket.socket()
        sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sk.bind((self.ip_port))
        sk.listen()
        while True:
            print('等待连接')
            conn, addr = sk.accept()
            print('连接成功')
            while True:
                ret=json.loads(conn.recv(1024).decode('utf-8'))
                if type(ret) ==list:
                    ip_port.register_login()
                elif ret==ls:
                    ip_port.cmd()
                elif ret==get:
                    ip_port.get()
            conn.close()
        sk.close()
    def register_login(self):
        config = configparser.ConfigParser()
        config.read('userinfo')
        user = (config.sections())
        username=ret[0]
        pwd=ret[1]
        for i in user:
            if i == username and config[username]['md5'] == pwd:
                conn.send('登录成功'.encode('utf-8'))

            else:
                conn.send('你输入的用户名或密码错误'.encode('utf-8'))


    def cmd(self):
        print('ls')
    def put(self):
        print('put')
    def get(self):
        print('get')
server=Server(('127.0.0.1',8090))
server.init_socket()
#ip_port.register_login()

#if __name__=='__main__':


