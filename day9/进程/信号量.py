from multiprocessing import Process,Semaphore
import time,random
def go_ktv(sem,user):
    sem.acquire()
    print('%s占到一件ktv小屋' %user)
    time.sleep(random.randint(3,5))
    sem.release()
    print('%s走出小屋'%user)
if __name__ == '__main__':
    sem=Semaphore(4)
    p_l=[]
    for i in range(13):
        p=Process(target=go_ktv,args=(sem,'user%s' %i,))
        p.start()
        p_l.append(p)
    for i in p_l:
        i.join()
    print('##########')
