#线程默认都是加了gil锁，在同一时刻，只能有一个线程访问cpu
import os
import time
from threading import Thread
n=100
def func(i):
    global n
    time.sleep(1)
    n-=1
    print(os.getpid(),'thread%s'%i)
l=[]
for i in range(100):
    p=Thread(target=func,args=(i,))
    p.start()
    l.append(p)
for t in l:
    t.join()
print(n)

# 什么是进程 ：是计算机资源分配的最小单位
# 什么是线程
# 线程和进程的关系 ：
    # 每一个进程中都至少有一个线程
# 每个进程里至少有一个主线程负责执行代码
# 在主线程中可以再开启一个新的线程
# 在同一个进程中就有两个线程同时在工作了
# 线程才是CPU调度的最小单位
# 多个线程之间的数据时共享的

#注意：使用多线程处理高计算的场景，python并不占优势，如果是高io类型的，就比较适合
#如：较多的网络请求，数据库请求，文件请求


