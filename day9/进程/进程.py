# 什么是进程 ： 运行中的程序，计算机中最小的资源分配单位
# 程序开始执行就会产生一个主进程
# python中可以主进程中用代码启动一个进程 —— 子进程
# 同时主进程也被称为父进程
# 父子进程之间的代码执行是异步的，各自执行自己的
# 父子进程之间的数据不可以共享
# 主进程会等待子进程结束之后再结束

#开启一个子进程
import os
import time
from multiprocessing import Process
# def func(num):
#     print(num,os.getpid())
#     time.sleep(0.5)
#     print(num,os.getpid())
#     time.sleep(0.5)
# if __name__ == '__main__':
#     p=Process(target=func,args=(10,))
#     p.start()
#     print(os.getpid())
#     time.sleep(1)
#     print(os.getpid(),1)

#父进程和子进程数据不可以共享，打印n为100
# n=100
# def func():
#     global n
#     n=0
#     print('------')
#     time.sleep(3)
# if __name__ == '__main__':
#     Process(target=func).start()
#     time.sleep(1)
#     print(n)

#开启多个子进程

# def func(n):
#     time.sleep(1)
#     print('_'*n)
# if __name__ == '__main__':
#     l=[]
#     for i in range(10):
#         p=Process(target=func,args=(i,))
#         p.start()
#         l.append(p)
#
#     print('子进程开始了')
#     for p in l:p.join()
#     print('10条信息已经发送完毕')

#守护进程
# 守护进程也是一个子进程
# 当主进程的代码执行完毕之后自动结束的子进程叫做守护进程

#当主进程结束的时候守护进程才结束
# def deamon_func():
#     while True:
#         print('我还活着')
#         time.sleep(0.5)
# def wahaha():
#     for i in range(10):
#         time.sleep(1)
#         print(i*'#')
# if __name__ == '__main__':
#     p2=Process(target=wahaha)
#     p2.start()
#     p=Process(target=deamon_func) #先执行这个
#     p.daemon=True
#     p.start()
#     for i in range(3):
#         print(i*'##')
#         time.sleep(1)
#     p2.join()

#当主进程代码执行结束之后，守护进程就结束
def deamon_func():
    while True:
        print('我还活着')
        time.sleep(0.5)
def wahaha():
    for i in range(10):
        time.sleep(1)
        print(i*'#')
if __name__ == '__main__':
    p2=Process(target=wahaha)
    p2.start()
    p=Process(target=deamon_func) #先执行这个
    p.daemon=True
    p.start()
    for i in range(3):
        print(i*'*')
        time.sleep(1)


# 开启一个子进程 start
# 子进程和主进程是异步
# 如果在主进程中要等待子进程结束之后再执行某段代码：join
# 如果有多个子进程 不能在start一个进程之后就立刻join，把所有的进程放到列表中，等待所有进程都start之后再逐一join
# 守护进程 —— 当主进程的"代码"执行完毕之后自动结束的子进程叫做守护进程


#
# def deamon_func():
#     while True:
#         print('我还活着')
#         time.sleep(0.5)
# if __name__ == '__main__':
#     p=Process(target=deamon_func)
#     p.daemon=True
#     p.start()
#     for i in range(3):
#         print(i*'#')
#         time.sleep(1)




