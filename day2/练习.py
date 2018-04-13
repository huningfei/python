#字符串
'''
name = "aleX leNb"
#8)	将name变量对应的值中的第一个’l’替换成’p’,并输出结果
# print (name[1])
a = name.replace('l','p',1)
print (a)

#9)	将 name 变量对应的值根据 所有的“l” 分割,并输出结果。

b = name.split('l')
print (b)

#11)	将 name 变量对应的值变大写,并输出结果
c = name.upper()
print (c)

#12)	将 name 变量对应的值变小写,并输出结果
d = name.lower()
print (d)

#13)	将name变量对应的值首字母’a’大写,并输出结果
e = name.capitalize()
print (e)
#14)	判断name变量对应的值字母’l’出现几次，并输出结果
f = name.count('l')
print (f)

#15)	如果判断name变量对应的值前四位’l’出现几次,并输出结果
# g = name.count('l','0','4')
#
# print (g)
#16)	从name变量对应的值中找到’N’对应的索引(如果找不到则报错)，并输出结果
j = name.index('N')
print (j)
#17)	从name变量对应的值中找到’N’对应的索引(如果找不到则返回-1)输出结果
j1 = name.find('N')
print (j1)

#18)	从name变量对应的值中找到’X le’对应的索引,并输出结果

# h = name.find('X', 'le')
# print (h)

#19)	请输出 name 变量对应的值的第 2 个字符?
h1 = name[1]
print (h1)

#20)	请输出 name 变量对应的值的前 3 个字符?
h2 = name[:3]
print (h2)

#21)	请输出 name 变量对应的值的后 2 个字符?
h3 = name[-2:]
print (h3)

#22)	请输出 name 变量对应的值中 “e” 所在索引位置?
h4 = name.find('e')
print (h4)
'''
'''

s = '123a4b5c'
#1)通过对li列表的切片形成新的字符串s1,s1 = ‘123’
s1 = s[0:3]
print (s1)
#2)通过对li列表的切片形成新的字符串s2,s2 = ‘a4b’
s2 = s[3:6]
print (s2)
#3)通过对li列表的切片形成新的字符串s3,s3 = ‘1345’
s3 = s[0:-1:2]
print (s3)

#4)通过对li列表的切片形成字符串s4,s4 = ‘2ab’
s4 = s[1:-2:2]
print (s4)
#5)通过对li列表的切片形成字符串s5,s5 = ‘c’
s5 = s[-1]
print (s5)
#6)通过对li列表的切片形成字符串s6,s6 = ‘ba2’
s6 = s[-3:0:-2]
print (s6)

#使用while和for循环分别打印字符串s=’asdfer’中每个元素。
b='asdfer'
'''

##列表
'''

li = ['alex','wusir','eric','rain','alex']
#1)计算列表的长度并输出

print(len(li))
#2)列表中追加元素’seven’,并输出添加后的列表
li.append('seven')
print (li)

#3)请在列表的第1个位置插入元素’Tony’,并输出添加后的列表
li.insert(0,'Tony')
print (li)

#4)请修改列表第2个位置的元素为’Kelly’,并输出修改后的列表
li[1] = 'kelly'
print (li)
#5)请将列表l2=[1,’a’,3,4,’heart’]的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
l2=[1,'a',3,4,'heart']
li.append(l2)
print (li)
#6)请将字符串s = ‘qwert’的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
s = 'qwert'
li.extend(s)
print (li)

#7)请删除列表中的元素’eric’,并输出添加后的列表
li.remove('eric')
print (li)
#8)请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
a1 = li.pop(1)
print (a1)
print (li)
#9)请删除列表中的第2至4个元素，并输出删除元素后的列表
del li[1:3]
print (li)
#10)请将列表所有得元素反转，并输出反转后的列表
li.reverse()
print (li)

#11)请计算出‘alex’元素在列表li中出现的次数，并输出该次数。
b = li.count('alex')
print (b)
'''
'''

#2，写代码，有如下列表，利用切片实现每一个功能
li = [1,3,2,'a','4','b','5','c']
c = li[-3:-1]
print (c)


#1)通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
l1 = li[:3]
print (l1)

#2)通过对li列表的切片形成新的列表l2,l2 = [’a’,4,’b’]
l2 = li[3:6]
print (l2)

#3)通过对li列表的切片形成新的列表l3,l3 = [’1,2,4,5]
l3 = li[:-1:2]
print (l3)

#4)通过对li列表的切片形成新的列表l4,l4 = [3,’a’,’b’]
l4 = li[1:-2:2]
print (l4)

#5)通过对li列表的切片形成新的列表l5,l5 = [‘c’]
l5 = li[-1:-3:-2]
print (l5)

#6)通过对li列表的切片形成新的列表l6,l6 = [‘b’,’a’,3]
l6 = li[-3:0:-2]
print (l6)

'''
#利用下划线将列表的每一个元素拼接成字符串"alex_eric_rain"

li = ['alex',' eric','wusir']
sa = '_'.join(li)
print (sa)

# for i in li:
#
#     i.strip()
#     print (i.strip())
#     i.startswith()
'''

#6开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符：
li = ["苍老师","东京热",'武藤兰','波多野结衣']

new_list=[]
m = input("请输入评论内容：").strip()
for i in li:
    if m == i:
        m=m.replace(i,'...')


        new_list.append(m)
else:
    new_list.append(m)
print (new_list)
'''

#5,查找列表li中的元素，移除每个元素的空格，
# 并找出以’A’或者’a’开头，并以’c’结尾的所有元素，并添加到一个新列表中,最后循环打印这个新列表。
# li = ['alex', ' aric', ' rain']
# new_list=[]
# for i in li:
#     m=i.strip()
#     print (m)
#     if m.startswith('a') or m.startswith('A'):
#         if m.endswith('c'):
#             new_list.append(m)
# print (new_list)

#有如下列表li = [1,3,4’,alex’,[3,7,8,’taibai’],5,’ritian’]
#循环打印列表中的每个元素，遇到列表则再循环打印出它里面的元素。
#我想要的结果是(用两种方法实现，其中一种用range做)：

li = [1,3,4,'alex',[3,7,8,'taibai'],5,'ritian']
# for i in li:
#    if type(i) == type([]):
#        print (i)
#
#
#    else:
#         for a in i:
#             print (a)

li = [1, 3, 4, 'alex', [3, 7, 8, 'taibai'], 5, 'ritian']

for i in li:
    if type(i) == type([]):
        for ii in i:
            print(ii)
    else:
        print(i)

#3,写代码，有如下列表，按照要求实现每一个功能。
















