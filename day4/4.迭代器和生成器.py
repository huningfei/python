# 迭代器
# 如何从列表、字典中取值的
    # index索引 ，key
    # for循环
# 凡是可以使用for循环取值的都是可迭代的
# 可迭代协议 ：内部含有__iter__方法的都是可迭代的
# 迭代器协议 ：内部含有__iter__方法和__next__方法的都是迭代器
# print(dir([1,2,3]))
# lst_iter = [1,2,3].__iter__()
# print(lst_iter.__next__())
# print(lst_iter.__next__())
# print(lst_iter.__next__())
# for i in [1,2,3]:   #  [1,2,3].__iter__()
#     print(i)
# l = [1,2,3]
# lst_iter = iter(l)   # l.__iter__()
# while True:
#     try:
#         print(next(lst_iter)) # lst_iter.__next__()
#     except StopIteration:
#         break

# 什么是可迭代的
# 什么是迭代器     迭代器 = iter(可迭代的)，自带一个__next__方法
# 可迭代 最大的优势 节省内存
# from collections import Iterable,Iterator
# print(range(100000000))
# print(isinstance(range(100000000),Iterable))
# print(isinstance(range(100000000),Iterator))
# py2 range 不管range多少 会生成一个列表 这个列表将用来存储所有的值
# py3 range 不管range多少 都不会实际的生成任何一个值
# 迭代器的优势:
#     节省内存
#     取一个值就能进行接下来的计算 ，而不需要等到所有的值都计算出来才开始接下来的运算 —— 快
# 迭代器的特性:惰性运算

# f = open()
# for line in f:

# 列表 字典 元组 字符串 集合 range 文件句柄 enumerate

# 生成器  Generator
# 自己写的迭代器 就是一个生成器
# 两种自己写生成器(迭代器)的机制：生成器函数 生成器表达式

# 生成器函数
# 200 0000
# 牛翔  200 0000
# 40期
# 赵英杰 200 0000
# 21 60  60件衣服
# 200 0000 - 60
# 500期  0
# 501

# def cloth(num):
#     ret = []
#     for i in range(num):
#         ret.append('cloth%s'%i)
#     return ret


# 凡是带有yield的函数就是一个生成器函数
# def func():
#     print('****')
#     yield 1
#     print('^^^^')
#     yield 2   # 记录当前所在的位置，等待下一次next来触发函数的状态
#
# g = func()
# print('--',next(g))
# print('--',next(g))
# 生成器函数的调用不会触发代码的执行，而是会返回一个生成器(迭代器)
# 想要生成器函数执行，需要用next
# def cloth_g(num):
#     for i in range(num):
#         yield 'cloth%s'%i
#
#
# g = cloth_g(1000)
# print(next(g))
# print(next(g))
# print(next(g))

# 使用生成器监听文件输入的例子
# import time
# def listen_file():
#     with open('userinfo') as f:
#         while True:
#             line = f.readline()
#             if line.strip():
#                 yield line.strip()
#             time.sleep(0.1)
#
# g = listen_file()
# for line in g:
#     print(line)

# send关键字
# def func():
#     print(11111)
#     ret1 = yield 1
#     print(22222,'ret1 :',ret1)
#     ret2 = yield 2
#     print(33333,'ret2 :',ret2)
#     yield 3
#
#
# g = func()
# ret = next(g)
# print(ret)
# print(g.send('alex'))  # 在执行next的过程中 传递一个参数 给生成器函数的内部
# print(g.send('金老板'))
# 想生成器中传递值 有一个激活的过程 第一次必须要用next触发这个生成器

# 例子
# 计算移动平均值
# 12 13 15 18
# 月度 的 天平均收入
# def average():
#     sum_money = 0
#     day = 0
#     avg = 0
#     while True:
#         money = yield avg
#         sum_money += money
#         day += 1
#         avg = sum_money/day
#
# g = average()
# next(g)
# print(g.send(200))
# print(g.send(300))
# print(g.send(600))

# 预激生成器
# def init(func):
#     def inner(*args,**kwargs):
#         ret = func(*args,**kwargs)
#         next(ret)  # 预激活
#         return ret
#     return inner
#
# @init
# def average():
#     sum_money = 0
#     day = 0
#     avg = 0
#     while True:
#         money = yield avg
#         sum_money += money
#         day += 1
#         avg = sum_money/day
#
# g = average()
# print(g.send(200))
# print(g.send(300))
# print(g.send(600))
#

# yield from
def generator_func():
    yield from range(5)
    yield from 'hello'
    # for i in range(5):
    #     yield i
    # for j in 'hello':
    #     yield j

# g = generator_func()
# for i in generator_func():
#     print(i)

g1 = generator_func()
g2 = generator_func()
next(generator_func())
next(generator_func())

# 如何从生成器中取值
# 第一种 ：next  随时都可以停止 最后一次会报错
# print(next(g))
# print(next(g))
# 第二种 ：for循环 从头到尾遍历一次 不遇到break、return不会停止
# for i in g:
#     print(i)
# 第三种 ：list tuple 数据类型的强转  会把所有的数据都加载到内存里 非常的浪费内存
# print(g)
# print(list(g))

# 生成器函数 是我们python程序员实现迭代器的一种手段
# 主要特征是 在函数中 含有yield
# 调用一个生成器函数 不会执行这个函数中的带码 只是会获得一个生成器（迭代器）
# 只有从生成器中取值的时候，才会执行函数内部的带码，且每获取一个数据才执行得到这个数据的带码
# 获取数据的方式包括 next send 循环 数据类型的强制转化
# yield返回值的简便方法，如果本身就是循环一个可迭代的，且要把可迭代数据中的每一个元素都返回 可以用yield from
# 使用send的时候，在生成器创造出来之后需要进行预激，这一步可以使用装饰器完成
# 生成器的特点 ： 节省内存 惰性运算
# 生成器用来解决 内存问题 和程序功能之间的解耦

# 列表推倒式
# new_lst = []
# for i in range(10):
#     new_lst.append(i**2)
# print(new_lst)
# print([i**2 for i in range(10)])
# l = [1,2,3,-5,6,20,-7]
# print([i%2 for i in range(10)])
# l = [1,2,3,-5,6,20,-7]
# print([num for num in l if num%2 == 1])

# 30以内所有能被3整除的数
# print([i for i in range(30) if i%3 ==0])
#
# 30以内所有能被3整除的数的平方
# print([i**2 for i in range(30) if i%3 ==0])

# 找到嵌套列表中名字含有两个‘e’的所有名字
# names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
#          ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
# print([name for name_lst in names for name in name_lst if name.count('e') == 2])

# 生成器表达式
# l = [i for i in range(30) if i%3 ==0]   # 列表推倒式 排序的时候
# g = (i for i in range(30) if i%3 ==0)   # 生成器表达式 庞大数据量的时候 使用生成器表达式
# print(l)
# print(g)
# for i in g:print(i)
# 林海峰

# 面试题
# def demo():
#     for i in range(4):
#         yield i
#
# g=demo()
#
# g1=(i for i in g)
# g2=(i for i in g1)
#
# print(list(g1))
# print(list(g2))

# def add(n,i):
#     return n+i
#
# def test():
#     for i in range(4):
#         yield i
#
# g=test()
# for n in [1,3,10]:
#     g=(add(n,i) for i in g)
#
# print(list(g))


# 一个生成器 只能取一次
# 生成器在不找它要值的时候始终不执行
# 当他执行的时候，要以执行时候的所有变量值为准



