from multiprocessing import Manager,Process,Lock
#manager 可以实现数据共享  (不重要）
def work(d,lock):
    with lock: #锁的简写
        d['count']-=1
if __name__ == '__main__':
    lock=Lock()
    m=Manager()
    dic=m.dict({'count':100})
    l=[]
    for i in range(10):
        p=Process(target=work,args=(dic,lock,))
        l.append(p)
        p.start()
    for p in l:
        p.join()
    print(dic)
