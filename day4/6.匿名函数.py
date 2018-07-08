# lambda表达式
# def add(a,b):
#     return a+b

# add = lambda a,b : a+b
# print(add(1,2))

# [i**2 for i in range(10)]
# def func(num):
#     return num ** 2
#
# # for i in map(func,range(10)):print(i)

# for i in map(lambda num : num ** 2 ,range(10)):print(i)

# def func(num):
#     return num%2
# print(min(-2,3,-4,key=func))

# print(min(-2,3,-4,key=lambda num:num%2))

# d = lambda p:p*2
# t = lambda p:p*3
# x = 2
# x = d(x)   # x = 4
# x = t(x)   # x = 12
# x = d(x)
# print(x)

# 现有两元组(('a'),('b')),(('c'),('d')),请使用python中匿名函数生成列表[{'a':'c'},{'b':'d'}]
# def func(t):
#     return {t[0]:t[1]}
# ret = map(func,zip((('a'),('b')),(('c'),('d'))))
# print(list(ret))

# ret = map(lambda t:{t[0]:t[1]},zip((('a'),('b')),(('c'),('d'))))
# print(list(ret))

# 3.以下代码的输出是什么？请给出答案并解释。
def multipliers():
    return [lambda x:i*x for i in range(4)]
print([m(2) for m in multipliers()])

# def multipliers():
#     lst = []
#     i = 0
#     lst.append(lambda x:i*x)
#     i = 1
#     lst.append(lambda x:i*x)
#     i = 2
#     lst.append(lambda x:i*x)
#     i = 3
#     lst.append(lambda x:i*x)
#     # lst = [lambda x:3*2,lambda x:i*x,lambda x:i*x,lambda x:i*x]
#     return lst
# print([m(2) for m in multipliers()])

# def multipliers():
#     return (lambda x:i*x for i in range(4))
g = (lambda x:i*x for i in range(4))
# print([m(2) for m in g])

# 请修改multipliers的定义来产生期望的结果。

#匿名函数和那些函数一起使用
#max,min,sorted,map,reduce,fiflter
