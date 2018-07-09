
# 1.使用lamda表达下面函数。
# def func(x, y):
#     return x+y
# print(func(2,3))
#
# ret = lambda x,y:x+y
# print(ret(2,3))

2#为这些基础函数加一个装饰器，执行对应函数内容后，
# 将当前时间写入一个文件做一个日志记录。
# import time
# def timer(f):
#   def inner(*args,**kwargs):
#     local_time = time.time()
#
# def foo():
#   print('hello foo')
#   return ()
#
#
# def bar():
#   print('hello bar')

#3. 通过内置函数计算5除以2的余数
#
#4. 现有两元祖  (('a'),('b'),('c'),('d') ) ,请使用Python中的匿名函数生成列表
# [ {'a':'c',{'c':'d'}]
# ret = map(lambda t:{t[0]:t[1]},zip((('a'),('b')),(('c'),('d'))))
# print(list(ret))

'''
#4 按年龄由大到小排列
alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
ret = sorted([i.get('age') for i in alist ],reverse=True)
print(ret)
'''
#6使用内置函数输出 [(1, 'h'), (2, 'e'), (3, 'l')]
# l1=[1,2,3,4]
# s='hel'
# ret = zip(l1,s)
# print(list(ret))

#7. 输出钱大于20的人名  结果为['IBM', 'Lenovo', 'oldboy']
shares = {
  "IBM": 36.6,
  "Lenovo": 23.2,
  "oldboy": 21.2,
  "ocean": 10.2
}

# ret = sorted(([i[0] for i in shares.items() if i[1] > 20]))
# print(ret)
#8. name=['alex','wupeiqi','yuanhao']
#将每个人名后加_sb 结果为['alex_sb','wupeiqi_sb','yuanhao_sb']
# name=['alex','wupeiqi','yuanhao']
# print([i+"_sb" for i in name])

#9. 	输出钱最多的人名  结果为alex
salaries={
	    'egon':3000,
	    'alex':100000000,
	    'wupeiqi':10000,
	    'yuanhao':250
}
# ret = sorted([i[0] for i in salaries.items()],reverse=True)
# print(ret)

# ret1 = sorted(salaries,key=lambda item:item[0])
# print(ret1[0])

print(max(salaries,key=lambda k:salaries[k]))


#10,2
print(sorted(salaries,key=lambda k:salaries[k]))





