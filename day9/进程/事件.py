# 事件内部内置了一个标志
# wait 方法 如果这个标志是True，那么wait == pass
# wait 方法 如果这个标志是False，那么wait就会陷入阻塞，一直阻塞到标志从False变成True

# 一个事件在创建之初 内部的标志默认是False
# Flase -> True set()
# True -> False clear()

# 红绿灯模型
from multiprocessing import Process, Event
import time, random

def car(e, n):
    while True:
        if not e.is_set():
            # 进程刚开启，is_set()的值是Flase，模拟信号灯为红色
            print('\033[31m红灯亮\033[0m，car%s等着' % n)
            e.wait()    # 阻塞，等待is_set()的值变成True，模拟信号灯为绿色
            print('\033[32m车%s 看见绿灯亮了\033[0m' % n)
            time.sleep(random.randint(3, 6))
            if not e.is_set():   #如果is_set()的值是Flase，也就是红灯，仍然回到while语句开始
                continue
            print('车开远了,car', n)
            break

def traffic_lights(e, inverval):
    while True:
        time.sleep(inverval)   # 先睡3秒
        if e.is_set():         # 标志是True
            print('######', e.is_set())
            e.clear()  # ---->将is_set()的值设置为False
        else:                 # 标志是False
            e.set()    # ---->将is_set()的值设置为True
            print('***********',e.is_set())


if __name__ == '__main__':
    e = Event()   #e就是事件
    t = Process(target=traffic_lights, args=(e, 3))  # 创建一个进程控制红绿灯
    for i in range(10):
        p=Process(target=car,args=(e,i,))  # 创建10个进程控制10辆车
        p.start()
    t.start()

    print('============》')



# 10个进程 模拟车 ：车的行走要依靠当时的交通灯
# 交通灯是绿灯 车就走
# 交通灯是红灯 车就停 停到灯变绿
# wait 来等灯
# set clear 来控制灯
