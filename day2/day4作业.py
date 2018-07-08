#li = ['alex','wusie','eric','rain','alex']
'''

#1)计算列表的长度并输出
print(len(li))
#2)列表中追加元素’seven’,并输出添加后的列表
li.append('senven')
print(li)
#33)请在列表的第1个位置插入元素’Tony’,并输出添加后的列表
li.insert(0,'Tony')
print(li)

#4)请修改列表第2个位置的元素为’Kelly’,并输出修改后的列表
li[1] = 'kelly'
print(li)
#5)请将列表l2=[1,’a’,3,4,’heart’]的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
l2=[1,'a',3,4,'heart']
li.extend(l2)
print(li)
'''

#7)请删除列表中的元素’eric’,并输出添加后的列表
# li.remove('eric')
# print(li)

#8)请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
# print(li.pop(2))
# print(li)

#9)请删除列表中的第2至4个元素，并输出删除元素后的列表
# del li [1:4]
# print(li)

#10)请将列表所有得元素反转，并输出反转后的列表
# li.reverse()
# print(li)

#11)请计算出‘alex’元素在列表li中出现的次数，并输出该次数。
#print(li.count('alex'))
'''

lis= [2,3,'k',['qwe',20,['k1',['tt',3,'1']],89],'ab','adv']
#1)将列表lis中的’tt’变成大写（用两种方式）。
# print(lis[3])
# print(lis[3][2][1][0].upper())  ##第一种
# lis[3][2][1][0] = "TT"  ##第二种
# print(lis[3][2][1][0])

#2)将列表中的数字3变成字符串’100’
lis[1] = 100
print(lis[1])


#3)将列表中的字符串’1’变成数字101
#第一种方法
# lis[3][2][1][2] = "101"
# print(lis[3][2][1][2])
#第二种方法：
lis[3][2][1][2] = int(lis[3][2][1][2]) + 100
print(lis[3][2][1][2])
'''

# li = ['alex','eric','rain']
# #利用下划线将列表的每一个元素拼接成字符串"alex_eric_rain"
# b = "_".join(li)
# print(b)


'''
##7循环打印列表中的每个元素，遇到列表则再循环打印出它里面的元素。 
li = [1,3,4,'alex',[3,7,8,'taibai'],5,'ritian']
for i in li:
    #print(type(i))
    print(i)
    if type(i) == list:
        for g in i:
            print(g)
'''

'''
##5 替换敏感词汇
li = ["苍老师", "东京热","武藤兰", "波多野结衣"]
new_list=[]
m = input("请输入你的评论：")
for i in li:
    if m == i:
        print("你输入的有敏感词汇")
        m = m.replace(i,'...')
        new_list.append(m)
    else:
        new_list.append(m)
print(new_list)
'''

'''
#6 查找列表li中的元素，移除每个元素的空格，并找出以’A’或者’a’开头，并以’c’结尾的所有元素，
# 并添加到一个新列表中,最后循环打印这个新列表。
li = ['taibai','alex','ABC','egon', 'Ritian','Wusir', ' aqc']
new_list = []
for i in li:
    b = (i.strip())
    if b.startswith("a") or b.startswith("A"):
        if b.endswith('c'):
            new_list.append(b)
print(new_list)

'''