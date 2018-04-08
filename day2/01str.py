s = 'python自动化21期'
# 切片
#s[起始索引:结束索引+1:步长]
# s1 = s[:6]
# print (s1)
#
# s2 = s[6:9]
# print (s2)

# print(s[0:])  ##默认到最后
#
# print (s[:-1]) ##-1代表最后一个，但是不打印最后一个
#
# print (s[0:5:2]) ##每隔1个打印一次 2 就代表步长
# print (s[5:0:-2])  ##反向加步长，倒着取值

# s = 'oldBoy'
# * capitalize()首字母大写，其他字母小写
s1 = s.capitalize()
# print (s1)
#

# *** 全部大写upper() 全部小写lower()
s2 = s.upper()
s3 = s.lower()
print (s2,s3)

#例子  输入验证码不区分大小写
# code = 'Qear'.lower()
# your_cold=input('请输入验证码：')
# if your_cold == code:
#     print ('验证成功')
# else:
#     print ('验证不成功')

#* 大小写反转 swapcase()
s4 = s.swapcase()
print (s4)

#*非字母的元素隔开的每个单词首字母大写 title()

ss = 'alex wusir*oldboy3taibia'
s5 = ss.title()
print (s5)

# center 居中，长度自己设定，默认填充物None
s6 = s.center(30,'*')
print (s6)

# *** startswith endswith 以什么开头，以什么结尾
s7 = s.startswith('o')
print (s7)  ##如果是真，则返回true

s8 = s.endswith('y')
print (s8)  ##同上

# *** strip 去除首尾的空格，制表符\t,换行符。不仅仅是去除空格....
# rstrip 去除右边，lstrip 去除左边

s = 'tyoyldBoyrte'
#
# print(s)
# s8 = s.strip()
# print(s8)
# s81 = s.strip('t')
# # print(s81)
# s81 = s.strip('tey')  ##把字符串里面的tey给去掉了，从左往右依次执行
# print(s81)

#例子：
# name = input('>>>').strip()  ##输入用户名的时候自动去除空格，可以防止用户输错
# if name == 'oldboy':
#     print('验证成功')

#*** split  (str ---> list)

# s1 = 'oldboy,wusir,alex'
# b = 'oldboywusiroalex'
# l = b.split()
# print(l)
# l = s1.split(',')  ##以逗号为分隔符，让s1变成了列表
# print(l)
# l2 = b.split('o')  # ['', 'ldb', 'ywusir', 'alex']b
# print(l2)
#
# l3 = b.split('o',1)  # ['', 'ldboywusiroalex']
# print(l3)


#join 将list --->str
sa = 'oldBoy'
s9 = '+'.join(sa)  ##用‘+’号把字符串连接起来
print(s9)
l1 = ['oldboy','wusir','alex']
s91 = '_'.join(l1) ##用'_'把字符串连接起来
print(s91)

# #replace 替换
h = '我们都是好孩子'
h1 = h.replace('我','你')
print(h1)

#find 通过元素找索引  找不到返回-1
# index 通过元素找索引 找不到报错

u = 'odlabced'
u1 = u.find('g')
print(u1)

# u2 = u.index('g')
# print (u2)

##字符串格式化输出format
# res='我叫{}今年{}岁，爱好{}'.format('egon',18,'male')
# print(res)
res='我叫{0}今年{1}岁，爱好{2},我依然叫{0}'.format('egon',18,'male')
print(res)
# res='{name} {age} {sex}'.format(sex='male', name='egon', age=18)
# print(res)

##公共方法
#len  count
n = 'dfdfdfdfsdfsf'
n1=len(n)
print (n1)  ##返回字符串的长度
n2 = n.count('d')  ##统计字母d出现了几次
print (n2)

##判断字符串的类型
name = 'jinxin989'
print (name.isalnum())  ## 判段字符串由字母或数字组成
print (name.isdigit())  ##是否只有字母
print (name.isalpha()) ##是否只有数字
#例子
i = '123a'
if i.isdigit():
    i = int(i)
else:
    print("输入有误...")


