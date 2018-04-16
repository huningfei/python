# def fun1():
#     print(111)
#     return
#     print(3333)
# fun1()

##函数的返回值
# s1 = "hello world"
# def mylen():
#     count = 0
#     for i in s1:
#         count += 1
#     return 555,444,count
# ret1,ret2,ret3 = mylen()
# print(ret1)
# print(ret2)
# print(ret3)

##函数的传参
# li = [1,2,3,4,'fdss','alex']
# s1 = 'dfdfdfd'
# def my_len(a):  ##函数的形参，可以随便写
#     count = 0
#     for i in a:
#         count += 1
#     return  count
# print(my_len(li))   ##函数的实参


#实参分为：位置参数，关键字参数，混合参数
#位置参数  ##一一对应，按顺序
# def func1 (x,y):
#     print(x,y)
# func1(1,2)
#
# ##关键字参数
# def func2 (x,y,z):
#     print(x,y,z)
# func2(y=2,x=1,z=3)
#
# #混合参数
# def func3(argv1,argv2,argv3):
#     print(argv1)
#     print(argv2)
#     print(argv3)
# func3(1,2,argv3=4)

#形参分为：位置参数，默认参数，动态参数
# 位置参数  一一对应，按顺序来
# def func1(x,y):
#     print(x,y)
# func1(1,2)

##默认参数
# def register(name,sex='男'):
#     with open('log1',encoding='utf-8',mode='a') as f1:
#         f1.write("{} {}\n".format(name,sex))
# register('aa')

 ##动态参数 *args  **kwargs
# def func2(*args,**kwargs):
#     print(args)  ##打印成元组
#     print(kwargs) ##打印成字典
# func2(1,2,2,3,4,5,'alex','老男孩',a='ww',b='qq')

#三种参数的排序

# def func3(a,b,*args,sex='男'):  ##顺序是 位置参数，*args ,默认参数
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
#     print(kwargs)
# func4(1,2,3,'alex','aa',sex='女',name='alex')


##打散 # 函数的执行：* 打散功能
def func1(*args,**kwargs):
    print(args)
    print(kwargs)
l1 = [1,2,3,4]
l11 = (1,2,3,4)
l2 = ['alex','wusir',4]
func1(*l1,*l2,*l11)    ##这个是以元组出现的

# def func1(*args,**kwargs):
#     print(args)
#     print(kwargs)
# dic1 = {'name1':'alex'}
# dic2 = {'name2':'wusir'}
# func1(**dic1,**dic2)   ##出来的结果是以字典形式存在的
