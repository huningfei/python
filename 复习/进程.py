from multiprocessing import Process
import time
#
#
# def task(name):
#     print('%s piaoing' % name)
#     time.sleep(2)
#     print("%s is down" % name)
#
#
# if __name__ == '__main__':  # windows上面开启进程必须写这个
#     # target目标，args传参
#     p = Process(target=task, args=('alex',))  # 开启一个进程
#     p1 = Process(target=task, args=('egon',))
#     p.start()  # 给操作系统发送一个指令
#     p1.start()
#     print("主")
#
# from threading import Thread
# import time
# def sayhi(name):
#     time.sleep(2)
#     print('%s say hello' %name)
#
# if __name__ == '__main__':
#     t=Thread(target=sayhi,args=('egon',))
#     t.start()
#     print('主线程')

from threading import Thread
from multiprocessing import Process
import os

def work():
    print('hello')

if __name__ == '__main__':
    #在主进程下开启线程
    t=Thread(target=work)
    t.start()
    print('主线程/')
    '''
    打印结果:
    hello
    主线程/主进程
    '''

    #在主进程下开启子进程
    t=Process(target=work)
    t.start()
    print('/主进程')
    '''
    打印结果:
    主线程/主进程
    hello
    '''
