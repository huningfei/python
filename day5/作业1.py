# import re
# def md(l, x):  ##计算乘法和除法
#     a = l.index(x)
#     if x == '*' and l[a + 1] != '-':
#         k = float(l[a - 1]) * float(l[a + 1])
#     elif x == '/' and l[a + 1] != '-':
#         k = float(l[a - 1]) / float(l[a + 1])
#     elif x == '*' and l[a + 1] == '-':
#         k = -(float(l[a - 1]) * float(l[a + 2]))
#     elif x == '/' and l[a + 1] == '-':
#         k = -(float(l[a - 1]) / float(l[a + 2]))
#     del l[a - 1], l[a - 1], l[a - 1]
#     l.insert(a - 1, str(k))
#     return l
#
#
# def fun(s): ##判断乘号和除号是否存在
#     l = re.findall('([\d\.]+|/|-|\+|\*)', s)
#     sum = 0
#     while 1:
#         if '*' in l and '/' not in l:
#             md(l, '*')
#         elif '*' not in l and '/' in l:
#             md(l, '/')
#         elif '*' in l and '/' in l:
#             a = l.index('*')
#             b = l.index('/')
#             if a < b:
#                 md(l, '*')
#             else:
#                 md(l, '/')
#         else:     ##计算加减法
#             if l[0] == '-':
#                 l[0] = l[0] + l[1]
#                 del l[1]
#             sum += float(l[0])
#             for i in range(1, len(l), 2):
#                 if l[i] == '+' and l[i + 1] != '-':
#                     sum += float(l[i + 1])
#                 elif l[i] == '+' and l[i + 1] == '-':
#                     sum -= float(l[i + 2])
#                 elif l[i] == '-' and l[i + 1] == '-':
#                     sum += float(l[i + 2])
#                 elif l[i] == '-' and l[i + 1] != '-':
#                     sum -= float(l[i + 1])
#             break
#     return sum
#
# def calculate(expression):
#     ex=[]
#     ans=0
#     if '(' not in expression:
#         ans=fun(expression)
#         return ans
#     for i in range(len(expression)):
#
#         if expression[i]=='(':
#             ex.append(i) #ex=[6,7] ##把(的索引加入到ex列表里面
#         elif expression[i]==')': #14
#             temp=0
#             sub=expression[ex[len(ex)-1]+1:i]
#             temp=fun(sub)
#             expression=expression[0:ex[len(ex)-1]]+str(temp)+expression[i+1:len(expression)+1]
#             ex.pop()
#             return calculate(expression)
# s='1 - 2 * ( (60-30 +(-40/5+3) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
# print(eval(s))
# print(calculate(s))

import re

# def multiply_divide(s):
#     if '*' in s:
#         a=float(s.split('*')[0]) * float(s.split('*')[1])
#     else:
#         b=float(s.split('/')[0]) / float(s.split('/')[1])
#     return b

# s='9*8*2*3'
# print(multiply_divide(s))

#def kuohao(biaodashi):  ##处理括号是否存在
    # if '(' not in biaodashi:
    #     c=check_rede_and_except(biaodashi)
    #
    # else:
    #     ret = res.search(biaodashi).group()
    #     biaodashi = biaodashi.replace(ret,str())
    #
    #     ##replace 括号里面的替换成计算好的结果，然后在交给上面的check_rede_and_except
    #     kuohao(biaodashi) ##递归去计算括号里面的


# import re
# dic = {
#     "*": lambda x,y : x * y,
#     "/": lambda x,y : x / y,
#     "+": lambda x,y : x + y,
#     "-": lambda x,y : x - y,
# }
# def substitute(m):
#     # print(m.group(), type(m.group()))   # 传递的是匹配到的字符串
#     lis_number = re.split("[\+\-\*\/]{1,}", m.group())   # 按符号切割2*5，得到["2", "5"]
#     # print(lis_number)
#     fuhao = re.findall("[\+\-\*\/]{1,}", m.group())[0]      # 得到这个切割符号, "+"
#     # print(fuhao)
#     value = dic.get(fuhao, ValueError)(float(lis_number[0]), float(lis_number[1]))  # 根据这个符号调用计算函数
#     return str(value)

# kh = '9-2*5/3+7/3*99/4*2998+10*568/14'
# kh = kh.strip("()")
#
# kh_new = re.sub("\d+\*\d+", substitute, kh)
# print(kh_new)


def multiply_divide(s):
    ret = float(s.split('*')[0]) * float(s.split('*')[1]) if '*' in s else float(s.split('/')[0]) / float(
        s.split('/')[1])
    return multiply_divide(s)
s='3*3*5'
print(multiply_divide(s))