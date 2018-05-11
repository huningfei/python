import re

res = re.compile(r'\([^()]+\)')  ##匹配最小单位的括号
input_filter = re.compile('[a-zA-Z]')


def check_rede_and_except(s):  ##检测表达式里面是否有乘除法
    s1 = s.replace(' ', '')
    l = re.findall('([\d\.]+|/|-|\+|\*)',
                   s1)  ##['100.5', '+', '40', '*', '5', '/', '2', '-', '3', '*', '2', '*', '2', '/', '4', '+', '9']
    while 1:
        if '*' in l and '/' not in l:
            ret = jisuan_rede_and_except(l, '*')

        elif '/' in l and '*' not in l:
            ret = jisuan_rede_and_except(l, '/')

        elif '/' in l and '*' in l:
            a = l.index('*')
            b = l.index('/')
            if a < b:
                ret = jisuan_rede_and_except(l, '*')
            else:
                ret = jisuan_rede_and_except(l, '/')
        else:
            break
    return jisuan_jia_and_jian(l)


def jisuan_rede_and_except(l, x):  ##计算乘除
    # print("l:%s %s:x" % (l,x))
    # print(l)
    a = l.index(x)
    if x == '*' and l[a + 1] != '-':
        k = float(l[a - 1]) * float(l[a + 1])
    elif x == '/' and l[a + 1] != '-':
        k = float(l[a - 1]) / float(l[a + 1])

    elif x == '*' and l[a + 1] == '-':
        k = -(float(l[a - 1]) * float(l[a + 2]))
    elif x == '/' and l[a + 1] == '-':
        k = -(float(l([a - 1])) / float(l[a + 2]))
    del l[a - 1], l[a - 1], l[a - 1]
    l.insert(a - 1, str(k))

    return l  ##['100.5', '+', '100.0', '-', '3.0', '+', '9'] 上面的ret接收到l


def jisuan_jia_and_jian(l):  ##计算加减
    sum = 0
    while l:  ##l=['100.5', '+', '100.0', '-', '3.0', '+', '9'] i=1,3,5

        if l[0] == '-':  ##['-','1','+','2']
            l[0] = l[0] + l[1]  ##l[0]=-1
            del l[1]  ##把1删除
        sum += float(l[0])
        for i in range(1, len(l), 2):  ##取出l列表里面的加减符号


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


def brackets(expression):  ##检查是否有括号
    if '*' not in expression and '/' not in expression:
        return check_rede_and_except(expression)
    if not res.search(expression):  # 匹配最里面的括号，如果没有的话，直接进行运算，得出结果
        return check_rede_and_except(expression)
    k = res.search(expression).group()  ##取出最小括号里面的值
    # print(k)

    expression = expression.replace(k, str(check_rede_and_except(k[1:len(k) - 1])))
    # print(expression)

    '''
        expression结果：
        1 - 2 * ( (60-30 +-5.0 * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
        1 - 2 * ( (60-30 +-5.0 * 173545.88095238098) - (-4*3)/ (16-3*2) )
        1 - 2 * ( -867699.4047619049 - (-4*3)/ (16-3*2) )
        1 - 2 * ( -867699.4047619049 - -12.0/ (16-3*2) )
        1 - 2 * ( -867699.4047619049 - -12.0/ 10.0 )
        1 - 2 * -867698.2047619049

    '''
    return brackets(expression)


#print('我是eval:%s'%(eval('1 - 2 * ( (60-30 +(-40/5+3) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )')))
#s= '1 - 2 * ( (60-30 +(-40/5+3) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
# # s2='9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14'
# #print(eval('9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14'))
# s='1+200'
# print(brackets(s))
# # check_rede_and_except(s2)
while True:
    # print("退出请按q\Q")
    s = input('请输入你想要计算的数字:')
    a = s.replace(' ', '')
    if input_filter.search(a) or a.count('(') != a.count(')'):
        print("你输入的表达式有误，请重新输入")
        continue
    if not a:continue
    print(brackets(a))


