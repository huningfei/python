# def wrapper():
#     def inner():
#         name1 = 'alex'
#         print(name1)
#     inner()
# wrapper()

# def wrapper():
#     name1 = 'wusir'
#     print(name1)
#     def inner():
#         name = 'alex'
#         print(name)
#     return inner
# ret = wrapper()
# ret()
 ##inner返回给了ret,所以直接执行ret()相当于执行了inner()

 ##测试一个函数执行效率

import time

# def func1():
# #     print('hello world')
# #     time.sleep(0.3)
# # ##最简单的装饰器
# # def timer(f1):  #f1 = func1
# #     def inner():
# #         start_time = time.time()
# #         f1()  ##相当于执行func1()
# #         end_time = time.time()
# #         print('此函数的执行效率%s' %(end_time - start_time))
# #     return inner  ##inner返回给了func1
# # func1 = timer(func1)
# # func1()   ##执行inner()


#@  第二种装饰器
# def timer(f1):
#     def inner():
#         start_time = time.time()
#         f1()
#         end_time = time.time()
#         print('此函数的执行效率是%s' % (end_time-start_time))
#     return inner
#
# @timer  ##func1 = timer(func1） =inner
# def func1():
#     print('hello world')
#     time.sleep(0.3)
# func1()  ##相当于执行了inner()  ,然后返回到上面 执行inner里面的语句，
# @timer
# def func2():
#     print('你好，世界')
#     time.sleep(0.4)
# func2()


##被装饰的函数带参数
# def timer(f1):  ##f1 = func1
#     def inner (*args,**kwargs):
#         start_time = time.time()
#         f1(*args,**kwargs)  ##func1函数是在这步开始执行的func1(111,222)
#         end_time = time.time()
#         print('此函数的执行效率是%s' %(end_time-start_time))
#     return inner
# @timer #func1 = timer(func1)  ##inner=func1
# def func1(a,b):
#     print(a,b)
#     print('hello world')
#     time.sleep(0.9)
# func1(111,222)  ##inner  把 111和222传给了上面的inner(*args）

##带返回值的装饰器
# def timer(f1):
#     def inner(*args,**kwargs):
#         start_time = time.time()
#         ret = f1(*args,**kwargs)  ##func1(111,222)
#         end_time = time.time()
#         print('此函数执行效率%s' % (end_time-start_time))
#         return ret  ##返回给了func1
#     return inner
# @timer  #func1 = timer(func1)
# def func1(a,b):
#     print(a,b)
#     print('hello world')
#     time.sleep(0.4)
#     return 666
# ret2 = func1(111,222)  ##inner(111,222)
# print(ret2)

def diary():
    a =  ('-----欢迎来到日记页面-----')
    return a
print(diary())