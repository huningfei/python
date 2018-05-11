import re
res = re.compile(r'\([^()]+\)')  # 匹配最小单位的括号
input_filter = re.compile('[a-zA-Z]')
def check_rede_and_except(s):
    '''
    检测表达式里面是否有乘除法
    :param s: 传进来的计算表达式
    :return: 返回一个没有乘除号的表达式
    '''
    l = re.findall('([\d\.]+|/|-|\+|\*)',s) # ['100.5', '+', '40', '*', '5', '/', '2', '-', '3', '*', '2', '*', '2', '/', '4', '+', '9']
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


def jisuan_rede_and_except(l, x):
    '''
     计算乘除
    :param l: 是带有乘除号的表达式
    :param x: 除号或者乘号
    :return: 返回一个没有乘除号的表达式
    '''

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

    return l  #['100.5', '+', '100.0', '-', '3.0', '+', '9'] 上面的计算加减的函数接收到l

def jisuan_jia_and_jian(l):
    '''
    计算加减
    :param l: 是一个只含有加减号的表达式
    :return: sum最终的计算结果
    '''
    sum = 0
    while l:  #l=['100.5', '+', '100.0', '-', '3.0', '+', '9'] i=1,3,5

        if l[0] == '-':  ##['-','1','+','2']
            l[0] = l[0] + l[1]  ##l[0]=-1
            del l[1]  # 把1删除
        sum += float(l[0])
        for i in range(1, len(l), 2):  #取出l列表里面的加减符号
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

def brackets(expression):
    '''
    检查是否有括号
    :param expression: 用户输入的表达式
    :return: 返回一个没有括号的表达式
    '''
    if not res.search(expression):  # 匹配最里面的括号，如果没有的话，去检测是否有乘除号
        return check_rede_and_except(expression)
    k = res.search(expression).group()  # 取出最小括号里面的值
    expression = expression.replace(k, str(check_rede_and_except(k[1:len(k) - 1])))
    # 把刚才计算的式子替换成计算的结果eg:2*3  替换成6 ，直到没有括号为止
    return brackets(expression)

print("\033[1;33m退出请按q\Q，运行请先查看readme\033[0m")
while True:

    s = input('请输入你想要计算的数字:')
    a = s.replace(' ', '')
    if a=='q' or a=='Q':
        break
    if input_filter.search(a) or a.count('(') != a.count(')'):
        print("\033[1;33m你输入的表达式有误，请重新输入\033[0m")
        continue
    if a=='':
        continue
    print(brackets(a))


