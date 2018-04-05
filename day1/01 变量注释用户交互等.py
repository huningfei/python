# 变量,将程序中运算的中间结果暂时存到内存中，以便后续程序调用。
BIRTH_OF_CHINA = 1949
x = 1+2+3+4
y = x*5 + 3
# print((1+2+3+4)*5 + 3)
'''
1,变量是由数字字母下划线任意组合。
2,变量不能是数字开头。
3,变量不能是Python中的关键字。
['and', 'as', 'assert', 'break', 'class',
'continue', 'def', 'del', 'elif', 'else',
 'except', 'exec', 'finally', 'for', 'from',
  'global', 'if', 'import', 'in', 'is', 'lambda',
  'not', 'or', 'pass', 'print', 'raise', 'return',
  'try', 'while', 'with', 'yield']
4，变量要具有可描述性。
    name,age,fdasgfdas
5,变量不能使用中文。
6，变量不能过长。
    AgeOfOldboy = 56
    NumberOfStudents = 80
#下划线
    age_of_oldboy = 56
    number_of_students = 80
'''
# age1 = 6
# age2 = age1
# age3 = age2
# age2 = 13
# print(age1, age2, age3)  # 6,13,6

#常量：一直不变的量。π，新中国成立 1949101
#约定俗成全部大写的变量为常量。放到文件最上面。
#注释：单行注释：#
# 多行注释：''' '''   """ """

# 基础数据类型：
'''
int:数字：计算。+ = * / % // .....

str:python中用引号引起来的就叫做字符串(''  "")。
    type(对象) 是什么数据类型
    用处：储存简单的少量数据。
    +    *
    + 字符串的拼接。
    * str* int
bool： True，Flase
'''
# print(666,type(666))
# print('666',type('666'))
# msg = "My name is Alex , I'm 56 years old!"
# msg = '''
# 今天我想写首小诗，
# 歌颂我的同桌，
# 你看他那乌黑的短发，
# 好像一只炸毛鸡。
# '''
# print(msg)
# a = '老男孩   '
# b = '是最好的培训机构'
# c = a + b
# print(c)
# print('坚强'*8)
# print(2 > 1)

# input 出来的数据类型全部是字符串。
# name = input('请输入您的姓名：')
# sex = input('请输入您的性别：')
# print('我的名字是' + name,'我的性别是' + sex)

msg =''' ------------ info of Alex Li -----------
Name  : Alex Li
Age   : 56
job   : Teacher
Hobbie: laddy_boy
------------- end -----------------
'''
#格式化输出 % 占位符  s  d
#ps  str -- > int  str全部由数字组成 ‘1234’
#ps  int -- > str  str(int)
#第一种表现形式：
# name = input('请输入你的名字：')
# age = input('请输入你的年龄：')
# job = input('请输入你的工作：')
# hobby = input('请输入你的爱好：')
# msg1 = ''' ------------ info of %s -----------
# Name  : %s
# Age   : %d
# job   : %s
# Hobbie: %s
# ------------- end -----------------
# ''' % (name,name,int(age),job,hobby)
# print(msg1)

#第二种方法：
# dic = {'name':'老男孩','age':45,'job':'Teacher','hobby':'吹'}
# msg1 = ''' ------------ info of %(name)s -----------
# Name  : %(name)s
# Age   : %(age)d
# job   : %(job)s
# Hobbie: %(hobby)s
# ------------- end -----------------
# ''' % dic
# print(msg1)
# msg2 = '我叫%s,今年%s,学习进度5%%' % ('太白',23)
# print(msg2)

#if 语句。
'''
if 条件:
    结果
'''
#1
# if 2 > 1 :
#     print(666)

#2
# if 2 < 1:
#     print(666)
# else:
#     print(555)

#3 多种条件选一个结果
# num = int(input('猜一下数字：'))
# if num == 6:
#     print('请你吃饭')
# elif num == 3:
#     print('请你喝酒')
# elif num == 1:
#     print('请你大保健')
#4 多种条件必选一个结果
# num = int(input('猜一下数字：'))
# if num == 6:
#     print('请你吃饭')
# elif num == 3:
#     print('请你喝酒')
# elif num == 1:
#     print('请你大保健')
# else:
#     print('没机会了.....')

# if 2 > 1:
#     if 2 < 1:
#         print(333)
#     else:
#         if '条件':
#             pass
#         print(666)

# score = int(input("输入分数:"))
# if score > 100:
#     print("我擦，最高分才100...")
# elif score >= 90:
#     print("A")
# elif score >= 60:
#     print("C")
# elif score >= 80:
#     print("B")
# elif score >= 40:
#     print("D")
# else:
#     print("太笨了...E")

#while 循环
'''
while 条件:
    结果
'''
# while True:
#     print('凉凉')
#     print('斗地主')
#     print('社会摇')
#     print('DJ大悲咒')

# 如何终止循环：
#1，改变条件。
#2，break
# count = 1
# while count <= 100:
#     print(count)
#     count = count + 1

# count = 1
# flag = True
# while flag:
#     print(count)
#     count = count + 1
#     if count == 101:
#         flag = False

# count = 1
# sum = 0
# while count < 101:
#     sum = sum +count
#     count += 1
# print(sum)

#while 关键字：break，continue
#break 结束循环。
#continue 跳出本次循环，继续下一次循环。
# while True:
#     print(333)
#     print(5455)
#     print(222)
#     break
#     print(888)
# print(666)

# while True:
#     print(333)
#     print(222)
#     continue
#     print(888)
# print(666)
#while else:如果while循环，被break打断，则不走else
# count = 1
# while count < 5:
#     print(count)
#     count += 1
# else:
#     print('循环正常完毕')
#逻辑运算符
#() > not > and > or
#前后都是比较运算 2 > 1 and 3 < 4 or 4 > 5 and 2 < 1
# print(2 > 1 and 3 < 4 or 4 > 5 and 2 < 1)  # True
# print(1 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)  # False
#前后都是数字
'''x or y if x is True,return x,else return y
int ---> bool  非0为True，0为Flase
'''
# print(3 or 2)
# print(2 or 6)
# print(0 or 6)
# print(3 and 5)
# print(1 > 2 or 3 and 4 > 5)

#dict
dic = {'name':'alex','age':12,'python21':['张三','李四']}
# print(dic['name'])
#list:  []
# li = [1,2,3,'alex']
# print(li[3])
#for 循环 有限循环。
li = [1,2,3,'alex']
s = 'fdsagfdagasd'
# for i in s:
#     print(i)
# for i in s:
#     if i == 'a':pass
#     print(i)
# else:
#     print(666)
'''
1、使用while循环输入 1 2 3 4 5 6     8 9 10

2、求1-100的所有数的和

3、输出 1-100 内的所有奇数

4、输出 1-100 内的所有偶数

5、求1-2+3-4+5 ... 99的所有数的和  奇数和偶数


'''
# 6、用户登陆（三次机会重试）
#input username password
#while i
#可以支持多用户登录
li = [{'username':'alex','password':'SB'},
    {'username':'wusir','password':'sb'},
    {'username':'taibai','password':'男神'},
      ]

#客户输入了三次机会，都没成功，给它一个选择，让它在试试
# Y 再给他三次机会...不输入了，print('臭不要脸.....')
# dic = {True:'alex',False:'SB'}
# dic = {(1,2,3):'alex',(2,3):'SB'}
# dic[(1,2,3)]