# # ##最简单的装饰器
# import time
#
# def func1():
#     print('hello world')
#     time.sleep(0.3)
#
# def timer(f1):  #因为下面timer(func1) 所以，#f1 = func1
#     def inner():
#         start_time = time.time()
#         f1()  ##相当于执行func1()
#         end_time = time.time()
#         print('此函数的执行效率%s' %(end_time - start_time))
#     return inner  ##inner返回给了func1
# func1 = timer(func1) #等于inner
# func1()   ##执行inner()

#第二种装饰器
import time
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
# @timer  #func1 = timer(func1） =inner
# def func2():
#     print('你好，世界')
#     time.sleep(0.4)
# func2()

#被装饰的函数带参数
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

#被装饰的函数带返回值
def timer(f1):
    def inner(*args,**kwargs):
        start_time = time.time()
        ret = f1(*args,**kwargs)  ##执行func1(111,222)
        end_time = time.time()
        print('此函数执行效率%s' % (end_time-start_time))
        return ret  ##返回给了func1
    return inner
@timer  #func1 = timer(func1) #func1接收了inner就是func1=inner
def func1(a,b):
    print(a,b)
    print('hello world')
    time.sleep(0.4)
    return 666
ret2 = func1(111,222)  ##inner(111,222)
print(ret2)