#定义一个函数
def mylen():
    s1='hello world'
    length=0
    for i in s1:
        length=length+1
    print(length)
mylen()

#函数的返回值
# def func1():
#     print(11)
#     print(22)
#     return
#     print(333)
#     print(444)
# func1()

#没有返回值
# def mylen():
#     """计算s1的长度"""
#     s1 = "hello world"
#     length = 0
#     for i in s1:
#         length = length+1
#     # print(length)
# str_len=mylen()
# print('str_len:%s'%str_len)

#一个返回值
# def mylen():
#     """计算s1的长度"""
#     s1 = "hello world"
#     length = 0
#     for i in s1:
#         length = length+1
#     return length
# str_len=mylen()
# print('str_len:%s'%str_len)

#返回多个值
# s1=(1,2,3,3)
# def my_len():
#     count = 0
#     for i in s1:
#         count += 1
#     return 666,222,count,'老男孩'
# print(my_len(),type(my_len()))

#返回多个值，用多个变量来接受
# def my_len():
#     count = 0
#     for i in s1:
#         count += 1
#     return 666,222,count
# ret1,ret2,ret3 = my_len()  # (666, 222, 19,)
# print(ret1)
# print(ret2)
# print(ret3)

#函数的传参
# li = [1, 2, 3, 43, 'fdsa', 'alex']
# s1 = 'fdsgdfkjlgdfgrewioj'
#
# def my_len(a):  # 函数的定义（）放的是形式参数，形参
#     count = 0
#     for i in a:
#         count += 1
#     return count
# ret = my_len(li)  # 函数的执行（） 实际参数，实参
# print(ret)
# print(len(s1))

# 实参分为：，
#位置参数必须一一对应，按顺序

'''
def func(x,y):
    print(x,y)
func(2,3)
'''


#关键字参数，必须一一对应，不分顺序
'''
def func(x,y,z):
    print(x,y,z)
func(y=4,z=2,x=1)
'''
#混合参数
'''
def func2(argv1,argv2,argv3):
    print(argv1,argv2,argv3)
func2(2,3,argv3=9)
'''

#形参分为：
#位置参数，必须一一对应
# def func(y,x):
#     print(y,x)
# func(1,2)
#默认参数,必须在位置参数后面
# def register(name,sex='男'):
#      with open('log1',encoding='utf-8',mode='a') as f1:
#          f1.write("{} {}\n".format(name,sex))
# register('hu')

#动态参数 *args，**kwargs
# kwargs接收的只是键值对的参数，并保存在字典中
#args接收除去键值对以外的所有参数,保存成元组形式
# def func2(*args,**kwargs):
#     print(args)  ##打印成元组
#     print(kwargs) ##打印成字典
# func2(1,2,2,3,4,5,'alex','老男孩',a='ww',b='qq')

#三种参数的和混合使用
# def func3(a,b,*args,sex='男'):  ##顺序是 位置参数（关键字），*args ,默认参数
#     print(a)
#     print(b)
#     print(sex)
#     print(args)
# func3(1,2,'老男孩','alex',sex='女')

# def func4(a,b,*args,sex='男',**kwargs): ##位置参数，*args,默认参数,**kwargs
#     print(a)
#     print(b)
#     print(args)
#     print(sex)
#     print(kwargs)#=
# func4(1,2,3,'alex','aa',sex='女',name='alex')

#打散
# def func1(*args,**kwargs):
#     print(args)
#     # print(kwargs)
# l1 = [1,2,3,4]
# l11 = (1,2,3,5)
# l2 = ['alex','wusir',4]
# func1(*l1,*l2,*l11)    ##这个是以元组出现的

# def func1(*args,**kwargs):
#     # print(args)
#     print(kwargs)
# dic1 = {'name1':'alex'}
# dic2 = {'name2':'wusir'}
# func1(**dic1,**dic2)   ##出来的结果是以字典形式存在的

#函数的命名空间

# name = 'wusir'  ##全局命名空间
# age = 12
# def func1():
#     name1 = 'bob'  ##局部命名空间
#     age1 = 34
#     return name1
# print(func1())
# print(name)

# name1 = 'wusir'
# def func1():
#     print(name1)
#     def func2():
#         print('xxxxx',name1)
#     func2()
# func1()

#查看命名空间
# name1 = 'wusir'
# def func1():
#  name2 = 'laonanhai'
#  print(globals())  ##查看全局变量
#  print(locals())  ##查看局部变量
# func1()

#global声明一个全局变量
# name = 'wusir'
# def func1():
#     global name  ##声明一个全局变量
#     name = 'alex'
#     return
# func1()
# print(name)  ##打印的结果是alex
# 对可变数据类型（list，dict，set）可以直接引用不用通过global。
# li = [1,2,3]
# dic = {'a':'b'}
#
# def change():
#     li.append('a')
#     dic['q'] = 'g'
#     print(dic)
#     print(li)
# change()

#nolocal不能修改全局变量
# def func2():
#     name1 = 'alex'
#     print('+',name1)#alex
#     def inner():
#         nonlocal name1
#         name1 = 'wusir'
#         print('*',name1)#wusir
#         def inner1():
#             pass
#     inner()
#     print('%',name1)#wusir
# func2()
#函数名

# #1 可以互相赋值
# def func1():
#     print(666)
# f1 = func1
# f1()

#2 函数名可以当成函数的参数
# def func1():
#     print(777)
# def func2(argv):
#     argv()
#     print(999)
# func2(func1)
# 打印结果是 777 999

#可以当成容器类数据类型的参数
# def func1():
#     print(666)
# def func2():
#     print(777)
# def func3():
#     print(888)
# ll = [func1,func2,func3]
# for i in ll:
#     i() #分别执行每个函数


#函数名可以当成函数的返回值
# def func1():
#     print(666)
# def func2(argv):
#     print(777)
#     return argv
# ret = func2(func1) ##func2执行  并且把func1传给了argv而argv又返回给了ret，所以ret=func1
# ret()  #结果是777 666

#闭包 内层函数对外层函数非全局变量的引用，叫做闭包

# def wrapper():
#     name1 = '老男孩'
#     def inner():
#         print(name1)
#     inner()
#     print(inner.__closure__)  ##如果返回是cell是闭包
# wrapper()
#
# name1 = '老男孩'
# def wrapper():
#
#     def inner():
#         print(name1)
#     inner()
#     print(inner.__closure__)  ##返回none不是闭包
# wrapper()

name = 'alex'
def wrapper(argv):
    def inner():
        print(argv)
    inner()
    print(inner.__closure__)  # cell
wrapper(name)