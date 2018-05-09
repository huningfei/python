# import re
# while True:
#     a = input("请输入你要计算的式子：")
#     res=re.split('[+]',a)
#     for i in res:
#         #print(i)
#         b=int(i)+int(i)
#     print(b)
#
#
# def jia():
#     pass
# def jian():
#     pass
# def cheng():
#     pass
# def chu():
#     pass
import re


def md(l, x): ##l是一个列表，x代表乘号和除号
    '''

    :param l: ['100.5', '+', '40', '*', '5', '/', '2', '-', '3', '*', '2', '*', '2', '/', '4', '+', '9']
    :param x: 取出所有的乘号和除号
    :return:
    '''
    a = l.index(x) ##获取运算符所在的索引
    #print(a)
    # print('我是l',l)
    # print('我是x',x)
    if x == '*' and l[a + 1] != '-':#判断*，/后面的一个操作符是否是‘-’如果是的话，分别进行处理
        k = float(l[a - 1]) * float(l[a + 1])
        #print(float(l[a-1]))
        # print(float(l[a+1]))
        #print(k)
    elif x == '/' and l[a + 1] != '-':
        k = float(l[a - 1]) / float(l[a + 1])
    elif x == '*' and l[a + 1] == '-':
        k = -(float(l[a - 1]) * float(l[a + 2]))
    elif x == '/' and l[a + 1] == '-':
        k = -(float(l[a - 1]) / float(l[a + 2]))
    print('我是第一个',l)
    del l[a - 1], l[a - 1], l[a - 1]
    #print('我是第二个',l)
    l.insert(a - 1, str(k))
    return l


def fun(s):
    l = re.findall('([\d\.]+|/|-|\+|\*)', s)
    sum = 0
    while 1:
        if '*' in l and '/' not in l:
            md(l, '*')
        elif '*' not in l and '/' in l:
            md(l, '/')
        elif '*' in l and '/' in l:
            a = l.index('*')
            b = l.index('/')
            if a < b:
                md(l, '*')
            else:
                md(l, '/')
        else:
            if l[0] == '-':
                l[0] = l[0] + l[1]
                del l[1]
            sum += float(l[0])
            for i in range(1, len(l), 2):
                if l[i] == '+' and l[i + 1] != '-':
                    sum += float(l[i + 1])
                elif l[i] == '+' and l[i + 1] == '-':
                    sum -= float(l[i + 2])
                elif l[i] == '-' and l[i + 1] == '-':
                    sum += float(l[i + 2])
                elif l[i] == '-' and l[i + 1] != '-':
                    sum -= float(l[i + 1])
            break
    return sum
print(eval('100.5+40*5/2-3*2*2/4+9'))
s= '100.5+40*5/2-3*2*2/4+9'
print(fun(s))