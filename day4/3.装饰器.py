# 装饰器
# 在原有的函数前后增加功能，且不改变原函数的调用方式

# 计算一个函数的运行之间
# import time
# def timmer(f):
#     def inner(*args,**kwargs):
#         start_time = time.time()
#         ret = f(*args,**kwargs)
#         end_time = time.time()
#         print(end_time - start_time)
#         return ret
#     return inner
#
# @timmer   # func = timmer(func)
# def func(a,b):
#     print('begin func',a)
#     time.sleep(0.1)
#     print('end func',b)
#     return True
#
# ret = func(1,2)   #--> inner()


# def timmer(f):
#     def inner(*args,**kwargs):
#
#         ret = f(*args,**kwargs)
#
#         return ret
#     return inner


# 进阶的需求
# 第一种情况
#     500个函数
#     你可以设计你的装饰器 来确认是否生效

# import time
# FLAG = True
# def outer(flag):
#     def timmer(f):
#         def inner(*args,**kwargs):
#             if flag == True:
#                 start_time = time.time()
#                 ret = f(*args,**kwargs)
#                 end_time = time.time()
#                 print(end_time - start_time)
#             else:
#                 ret = f(*args, **kwargs)
#             return ret
#         return inner
#     return timmer
#
# @outer(FLAG)   # func = timmer(func)
# def func(a,b):
#     print('begin func',a)
#     time.sleep(0.1)
#     print('end func',b)
#     return True
#
# func(1,2)


# 第二种情况
def wrapper1(func):
    def inner1():
        print('wrapper1 ,before func')
        func()
        print('wrapper1 ,after func')
    return inner1

def wrapper2(func):
    def inner2():
        print('wrapper2 ,before func')
        func()
        print('wrapper2 ,after func')
    return inner2

@wrapper2
@wrapper1
def f():
    print('in f')

# f()



# 装饰器 登录 记录日志
import time
login_info = {'alex':False}
def login(func):   # manager
    def inner(name):
        if login_info[name] != True:
            user = input('user ：')
            pwd = input('pwd ：')
            if user == 'alex' and pwd == 'alex3714':
                login_info[name] = True
        if login_info[name] == True:
            ret = func(name)     # timmer中的inner
            return ret
    return inner

def timmer(f):
    def inner(*args,**kwargs):
        start_time = time.time()
        ret = f(*args,**kwargs)     # 调用被装饰的方法
        end_time = time.time()      #
        print(end_time - start_time)
        return ret
    return inner

@login
@timmer
def index(name):
    print('欢迎%s来到博客园首页~'%name)

@login
@timmer    # manager = login(manager)
def manager(name):
    print('欢迎%s来到博客园管理页~'%name)

index('alex')
index('alex')
manager('alex')
manager('alex')

# 计算index 和 manager的执行时间

