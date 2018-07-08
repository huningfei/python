# 自定义函数
# 内置函数
    # print
    # len
    # max min
    # dir


# def func():
#     a = 1
#     b = 2
#     print(locals())
#     print(globals())
# 全局命名空间中的名字
# print(locals())   # 本地的命名空间
# print(globals())  # 全局的命名空间
# func()

# inp = input('>>>')
# 99乘法表
# for i in range(1,10):
#     for j in  range(1,i+1):
#         print('%s * %s = %2s'%(i,j,i*j),end=' ')
#     print()

# print(1,2,3,4,5,sep=';',end='  ')
# print(1,2,3,4,5,sep=';',end='')

# import time
# for i in range(0,101,2):  #0,2,4,6,8
#      time.sleep(0.1)
#      char_num = i//2      #打印多少个'*'     4
#      if i == 100:
#          per_str = '\r%s%% : %s\n' % (i, '*' * char_num)
#      else:
#         per_str =  '\r%s%% : %s'%(i,'*'*char_num)
#      print(per_str,end='',flush=True)   # 0.01

# print()    写文件
# python 能直接操作文件 —————— 需要发起系统调用 才能操作文件

# print(hash('1291748917'))
# print(hash('1291748917'))

#对可hash的数据类型进行hash之后会得到一个数字
# 在一次程序的执行过程中 对相同的可哈希变量 哈希之后的结果永远相同的
# 在一次程序的执行过程中 对不相同的可哈希变量 哈希之后的结果几乎总是不相同的
# hash 字典底层的存储 和set 集合的去重机制 都相关

# id()

# callable 可调用
# def func():pass
# a = 1
# print(callable(func))
# print(callable(a))

# print(dir('1')) # 查看一个变量所拥有的所有名字

# print(bin(10))
# print(oct(10))
# print(hex(10))  # 0123456789abcdef

# print(abs(4))
# print(abs(-4))

# print(divmod(10,2))  # 商余函数
# print(divmod(7,3))  # 商余函数
# print(divmod(9,7))  # 商余函数
# 返回一个元组

# print(round(3.1415926,4)) # 默认取整，小数精确 会四舍五入

# print(pow(2,3,5))  # (2**3)%5
# print(pow(3,2,2))

# print(sum([1,2,3,4,5]))
# print(sum([1,2,3,4,5],start=0))
# print(sum([1,2,3,4,5],start=20))
# print(sum(range(1,6)))

# print(min([1,2,3,4,5]))
# print(min(1,2,3,4))
# print(min(1,-2,3,-4))
# print(min(1,-2,3,-4,key=abs))
# def func(num):
#     return num%2
# print(min(-2,3,-4,key=func))

# ret = [1,2,3,4,5]
# ret.reverse()
# print(ret)

# ret1 = reversed(ret)
# ret2 = reversed((1,2,3,4,5))
# print(ret)
# print(list(ret1))
# print(list(ret2))

# print(format('test', '<20'))
# print(format('test', '>20'))
# print(format('test', '^20'))

# print(ord('a'))    # 小写的a-z 97+26  A-Z 65+26
# print(chr(97))

# print(1)
# print('1')
# print(repr(1))
# print(repr('1'))

# l = ['苹果','香蕉']
# # ret = enumerate(l,1)   # 枚举  接收两个参数：一个容器类型，一个序号起始值   返回值：可迭代的
# # print(ret)
# for num,item in enumerate(l,1):
#     print(num,item)

# print(all([1,2,3,4,5]))
# print(all([0,1,2,3,4,5]))
# print(all(['a',1,2,3,4,5]))
# print(all(['',1,2,3,4,5]))
# print(any([0,None,False]))

# ret = zip([1,2,3,4,5],('a','b','c','d'),(4,5))   #拉链方法
# print(ret)
# for i in ret:
#     print(i)

#
lst =  [1, 4, 6, 7, 9, 12, 17]
# def func(num):
#     if num % 2 == 0:return True
# filter(func,lst)
# for i in filter(func,lst):
#     print(i)
# g = (i for i in lst if i%2 == 0)

# l = ['test', None, '', 'str', '  ', 'END']
# def func(item):
#     if item and item.strip():return True
# for i in filter(func,l):
#     print(i)


# [i**2 for i in range(10)]
# def func(num):
#     return num ** 2
# for i in map(func,range(10)):print(i)

# 排序功能
# l = [1,-4,-2,3,-5,6,5]
# l.sort(key=abs)
# print(l)
# l = [1,-4,-2,3,-5,6,5]
# new_l = sorted(l,key=abs,reverse=True)
# print(new_l)

# l = [[1,2],[3,4,5,6],(7,),'123']
# # print(sorted(l,key=len))

# eval()
# eval('print(123)')
# exec('print(123)')
# print(eval('1+2-3*20/(2+3)'))
# print(exec('1+2-3*20/(2+3)'))


# 内置函数
# 标红的如果不会
# 标黄的 是能够节省你的代码 面试会用
# min max sorted filter map 面试明星知识点
# 你经常不见 且没被点名说重点的 就不用特别了解了

