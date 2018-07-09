#提交任务的两种方式：
#同步调用：提交完任务后，就在原地等待，等待任务执行完毕，拿到任务的返回值，才能继续下一行代码，导致程序串行执行
#异步调用+回调机制：提交完任务后，不在原地等待，任务一旦执行完毕就会触发回调函数的执行， 程序是并发执行
import time
from concurrent.futures import ProcessPoolExecutor
import random,os
# def func(num):
#     print(num)
#     time.sleep(1)
#     print(num)
# if __name__ == '__main__':
#     t=ProcessPoolExecutor(20)#开启20个进程
#     for i in range(50):
#         t.submit(func,i)
#     t.shutdown()
#     print('done')

#同步调用
def task(n):
    print('%s is runing'%os.getpid())
    time.sleep(random.randint(1,3))
    return n**2
def handle(res):
    print('handle res %s' %res)
if __name__ == '__main__':
    pool=ProcessPoolExecutor(3)
    for i in range(5):
        res=pool.submit(task,i).result()
        handle(res)
    pool.shutdown()
    print('主')
#异步调用
# def task(n):
#     print('%s is runing'%os.getpid())
#     time.sleep(random.randint(1,3))
#     return n**2
# def handle(res):
#     res=res.result()
#     print('handle res %s' %res)
# if __name__ == '__main__':
#     pool=ProcessPoolExecutor(2)
#     for i in range(5):
#         obj=pool.submit(task,i)
#         obj.add_done_callback(handle)
#
#     pool.shutdown()
#     print('主')
