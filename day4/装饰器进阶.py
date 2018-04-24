##装饰器
##同时管理多个被装饰的函数是否执行这个装饰器
# import time
# flag = True
# def manage(flag):
#     def timer(f1):
#         def inner(*args,**kwargs):
#             if flag == True:
#                 start_time = time.time()
#                 ret = f1(*args,**kwargs)  ##func()
#                 end_time = time.time()
#                 print("这个函数花费了%s" %(end_time-start_time))
#                 return ret
#             else:
#                 ret = f1(*args, **kwargs)
#                 return ret
#         return inner
#     return timer
# @manage(flag) ##func=timer(func)  ##inner
# def func(a,b):
#     print("heloo word")
#     print(a,b)
#     time.sleep(0.1)
#     return 222
# ret2 = func(222,333)##inner(222,333）
# print(ret2)


'''
##两个装饰器装饰一个函数
def wrapper1(f1):  ##第三部 func
    def inner1(*args,**kwargs):
        print("我是wrapper1,func before")  ##第二部
        ret = f1(*args,**kwargs)  ##inner2
        print("我是wrapper1,func after")
        return ret
    return inner1  ##第四步，返回给wraper1

def wrapper2(f1):  ##第七步 f1 = inner1
    def inner2(*args,**kwargs):  ##第十一
        print("我是wrapper2,func before")
        ret = f1(*args,**kwargs)  ##inner1
        print("我是wrapper,func after ")
        return ret
    return inner2  ##第八步 inner2返回给了wrapper2
@wrapper2 第五步 f=wrapper2(f)  == f=wrapper2(inner1)##执行了inner1 f=inner2
@wrapper1  ##第二步 f = wrapper1(f)   f = wrapper1(inner1) f=inner1
def func():## 第一步
    print("我是func")
func()  ##第十部 即func() == inner2()
'''

import time
login_info = {'alex': False}
def login(func):  # manager
    def inner(name):
        if login_info[name] != True:
            user = input('user ：')
            pwd = input('pwd ：')
            if user == 'alex' and pwd == 'alex3714':
                login_info[name] = True
        if login_info[name] == True:
            ret = func(name)  # timmer中的inner
            return ret

    return inner


def timmer(f):  ##第三步  f= index
    def inner(*args, **kwargs):
        start_time = time.time()
        ret = f(*args, **kwargs)  # 调用被装饰的方法
        end_time = time.time()  #
        print(end_time - start_time)
        return ret
    return inner  ##第四部
@login  ##第六部：index=login(index)  == inner=login(inner)
@timmer  ##第二部  index = timmer(index)  第五步：index = inner
def index(name):   ##第一步
    print('欢迎%s来到博客园首页~' % name)


@login
@timmer  # manager = login(manager)
def manager(name):
    print('欢迎%s来到博客园管理页~' % name)


index('alex')
index('alex')
manager('alex')
manager('alex')




