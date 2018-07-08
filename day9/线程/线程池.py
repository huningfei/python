#线程池
# import time
# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
# def func(num):
#     print(num)
#     time.sleep(1)
#     print(num)
# if __name__ == '__main__':
#     t=ThreadPoolExecutor(20)
#     for i in range(50):
#         t.submit(func,i)
#     t.shutdown()
#     print('done')
#map的简便用法
# import os,time,random
# from concurrent.futures import ThreadPoolExecutor
# def task(n):
#     print('%s is runing' %os.getpid(),n)
#     time.sleep(random.randint(1,3))
#     return n**2
# if __name__ == '__main__':
#     executor=ThreadPoolExecutor(max_workers=3)
#     # for i in range(11):
#     #     future=executor.submit(task,i)
#     executor.map(task,range(1,12)) #map取代了for+submit #把1到12都赋值给n

#callback(回调函数)
# import time
# import random
# from concurrent.futures import ThreadPoolExecutor
# from threading import current_thread
# urls=[
#         'https://www.baidu.com',
#         'https://www.python.org',
#         'https://www.openstack.org',
#         'https://help.github.com/',
#         'http://www.sina.com.cn/'
#         'http://www.cnblogs.com/'
#         'http://www.sogou.com/'
#         'http://www.sohu.com/'
#     ]
#
# def analies(content):
#     print('分析网页',current_thread())
#     print(content.result())
#
#
# def get_url(url):
#     print('爬取网页',current_thread())
#     time.sleep(random.uniform(1,3))
#     # analies(url*10)
#     return url*10
#
# t = ThreadPoolExecutor(3)
# print('主线程',current_thread())
# for url in urls:
#     t.submit(get_url,url).add_done_callback(analies) #
#回调函数当执行了get_url之后，得到了一个url*10 ,然后在立即执行analies函数，并传给content参数

# concurrent.futures里面的 callback是由子线程做的







#进程池
# import time
# from concurrent.futures import ProcessPoolExecutor
# def func(num):
#     print(num)
#     time.sleep(1)
#     print(num)
# if __name__ == '__main__':
#     t=ProcessPoolExecutor(20)
#     for i in range(50):
#         t.submit(func,i)
#     t.shutdown()
#     print('done')