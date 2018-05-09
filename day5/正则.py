# \w{2,}?  ##匹配两次，问号是惰性匹配
# \w{2,} #匹配两次或更多次
# \w{2,3} ##匹配两次到三次因为是贪婪匹配，所以默认匹配三次
# https://www.cnblogs.com/Wxtrkbc/p/5453349.html
# https://www.cnblogs.com/wushank/p/5172792.html
# import re
# expression='(( 100 + 40 )*5/2- 3*2* 2/4+9)*((( 3 + 4)-4)-4)'
# l=re.findall('([\d\.]+|/|-|\+|\*)',expression)
# print(l)

import re
expression= '100.5+40*5/2-3*2*2/4+9'
l = re.findall('([\d\.]+|/|-|\+|\*)',expression)
#print(100.5+40*5/2-3*2*2/4+9)                     # 206.5
def multdiv(l,x):                                 #定义最小的乘除运算单元，l是列表，x代表*或/
    a = l.index(x)                                #首先获取乘除运算符的位置
    if x=='*':                                    #如果是*则执行乘法运算
        k = float(l[a - 1]) * float(l[a + 1])     #获取乘法运算的结果，比如k=3*2
    else:
        k = float(l[a - 1]) / float(l[a + 1])
    del l[a - 1], l[a - 1], l[a - 1]              #删除掉列表里刚做运算的三个元素，比如，3 * 2
    l.insert(a - 1, str(k))                       #将刚计算的结果插入到列表中然后执行下一次计算
    print(l)

