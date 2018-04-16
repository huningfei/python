##函数里面声明的变量叫临时名称空间，存入函数里面的变量与值的关系，随着函数的执行结束，
# 临时名称空间消失

# name = 'wusir'  ##全局命名空间
# age = 12
# def func1():
#     name1 = 'wusir'  ##局部命名空间
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


# name1 = 'wusir'
# def func1():
#     name2 = 'laonanhai'
#     print(globals())  ##查看全局变量
#     print(locals())  ##查看局部变量
# func1()

##global  nonlocal 关键字

#global  ##声明一个全局变量(限于字符串，数字)
# name = 'wusir'
# def func1():
#     global name  ##声明一个全局变量
#     name = 'alex'
#     return
# func1()
# print(name)  ##打印的结果是alex

#对可变数据类型（list，dict，set）可以直接引用不用通过global。
# li = [1,2,3]
# dic = {'a':'b'}
#
# def change():
#     li.append('a')
#     dic['q'] = 'g'
#     print(dic)
#     print(li)
# change()
# print(li)
# print(dic)

#nonlocal  ##1不能修改全局变量
#2在局部作用域中，对父级作用域（或者更外层作用域非全局作用域）的变量进行引用和修改，
# 并且引用的哪层，从那层及以下此变量全部发生改变

# def func2():
#     name1 = 'alex'
#     print('+',name1)
#     def inner():
#         nonlocal name1
#         name1 = 'wusir'
#         print('*',name1)
#         def inner1():
#             pass
#     inner()
#     print('%',name1)
# func2()

##函数名（就是def后面的那个字符串）
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

#可以当成容器类数据类型的参数
# def func1():
# #     print(666)
# # def func2():
# #     print(777)
# # def func3():
# #     print(888)
# # ll = [func1,func2,func3]
# # for i in ll:
# #     i()

#函数名可以当成函数的返回值
# def func1():
#     print(666)
# def func2(argv):
#     print(777)
#     return argv
# ret = func2(func1)
# ret()

# 闭包 内层函数对外层函数非全局变量的引用，叫做闭包
#闭包的好处：如果python 检测到闭包，
# 他有一个机制，你的局部作用域不会随着函数的结束而结束
##闭包
# def wrapper():
#     name1 = '老男孩'
#     def inner():
#         print(name1)
#     inner()
#     print(inner.__closure__)  ##如果返回是cell是闭包
# wrapper()

# name1 = '老男孩'
# def wrapper():
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