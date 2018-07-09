from threading import Thread
import time
def foo():
    while 1:
        print(123)
        time.sleep(1)
def bar():
    print(456)
    time.sleep(5)
    print('end456')
t1=Thread(target=foo)
t2=Thread(target=bar)
t1.daemon=True  #t1是守护线程，t2是主线程
t1.start()
t2.start()
print('#####') #主线程
# 主线程结束了之后守护线程也同时结束
# 守护线程会等待主线程完全结束之后才结束


#递归锁（Rlock）
from threading import RLock

lock = RLock()
lock.acquire()
lock.acquire()
print(123)
lock.release()
print(456)
lock.release()