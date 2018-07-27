#  一 内置函数
#
# 1 输出 print

# print(1,2,3,4,5,sep=';',end='| ') ##sep是以;分开每个数字，end是以|结尾的

#绝对值
# print(abs(-9))
#divmod返回商和余数
# print(divmod(9,4))
# print(pow(2,3,5)) #（2**3） 就是2的三次方，对5取余 8%5

#min最小值
# print(min(-1,0,3,4))
#
# print(min(-1,0,3,4,key=abs)) ##算完绝对值之后，在返回最小值

#eval和exec
# eval('print(123)')
# exec('print(123)')
#
# print(eval('1+2-3*20/(2+3)'))##有返回值
# print(exec('1+2-3*20/(2+3)')) ##执行了但没有返回值

#format格式化显示，后面的数字代表距离
# print(format('test', '<2'))
# print(format('test', '>20'))
# print(format('test', '^40'))

# ord字符串转数字
# print(ord('b'))
##repr用于%r格式化输出

# print(repr(1))
# print(1)
#
# print(repr('1'))

#enumerate枚举
# ll=['a','b','c']
# for i,v in enumerate(ll):
#     print(i,v)

#zip拉链

ret = zip([1, 2, 3, 4, 5], ('a', 'b', 'c', 'd'), (4, 5,0))  # 拉链方法

print(ret)

for i in ret:
    print(i)

#filter 重要  用于过滤，比如大于几的数字，或者偶数，奇数之类的
lst = [1, 4, 6, 7, 9, 12, 17]
def func(num):
    if num % 2 == 0: return True

filter(func, lst)  ##分别把lst里面的值传给num，然后取出除2等于0的数字

for i in filter(func, lst):

    print(i)


##第二种方法
g = (i for i in lst if i%2 == 0)
for i in g:
    print(i)

#map求平方
def func(num):

    return num**2
for i in map(func,range(10)):

    print(i)

# sorted排序（重要）
# l = [1,-4,-2,3,-5,6,5]
#
# new_l = sorted(l,key=abs,reverse=True) ##按照绝对值大小，并且反序来排序的
#
# print(new_l)

# 二 匿名函数
# calc = lambda n:n**n
# print(calc(2))
#
# rs=lambda n,p:n**p
# print(rs(2,3))

# for i in map(lambda num : num ** 2 ,range(10)):print (i) #打印1-9 ，9个数字的平方
# 现有两元组(('a'),('b')),(('c'),('d')),请使用python中匿名函数生成列表[{'a':'c'},{'b':'d'}]
ret = map(lambda t:{t[0]:t[1]},zip((('a'),('b')),(('c'),('d'))))
print(list(ret))