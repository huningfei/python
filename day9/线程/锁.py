from threading import Thread,Lock
import time
def work():
    global n

    lock.acquire()
    temp=n
    time.sleep(0.1)
    n=temp-1
    lock.release()
if __name__ == '__main__':
    lock = Lock()
    n=100
    l=[]
    for i in range(10):
        p=Thread(target=work)
        l.append(p)
        p.start()
    for i in l:
        i.join()
    print(n)


# 当你的程序中出现了取值计算再赋值的操作 数据不安全 —— 加锁

