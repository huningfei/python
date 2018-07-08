# from socket import *
# from multiprocessing import Process
# server=socket()
# server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# server.bind(('127.0.0.1',8080))
# server.listen()
# def talk(conn,client_addr):
#     while True:
#         try:
#             msg=conn.recv(1024)
#             if not msg:break
#             conn.send(msg.upper())
#         except Exception:
#             break
# if __name__ == '__main__':
#     while True:
#         conn,client_addr=server.accept()
#         p=Process(target=talk,args=(conn,client_addr))
#         p.start()

from socket import *
from multiprocessing import Pool
import os

server=socket()
server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) #地址可以重用
server.bind(('127.0.0.1',8080))
server.listen(5)

def talk(conn):
    print('进程pid: %s' %os.getpid())
    while True:
        try:
            msg=conn.recv(1024)
            if not msg:break
            conn.send(msg.upper())
        except Exception:
            break

if __name__ == '__main__':
    p=Pool(4)
    while True:
        conn,*_=server.accept()
        p.apply_async(talk,args=(conn,))