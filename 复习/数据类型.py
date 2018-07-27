#切片
# s = 'python自动化21期'
# s1=s[1:3]
# print(s[1:6:2])
# print(s[0:])
# # 打印到最后但是不包括最后一个
# print(s[:-1])
# print(s[6:0:-2])
#capitalize大小写
s2='hu'
# s1=s2.capitalize()
# print(s1)

# print(s2.upper())
# print(s2.lower())
# print(s2.swapcase())

#title

# ss = 'alex wusir*oldboy3taibiahu'
# print(ss.title())
#
# print(s2.center(30,'*')) #**************hu**************

#strip
# s = 'tyoyldBoyrte'
# s1='hkdjkltkjkedfdty'
# print(s)
# print(s.strip())
# print(s1.strip('tey'))
#
# name=input('>>>').strip()
# if name == 'hu':
#     print('登录成功')
# split   以什么分割，最终形成一个列表此列表不含有这个分割的元素
# b = 'oldboywusiroalex'
# l = b.split()  # 字符串变成列表
# print(l)
# s1 = 'oldboy,wusir,alex'
# print(s1.split(','))# 字符串变成列表
#
# l3 = b.split('o',3)#以o分割，最终形成3个列表
# print(l3)

#join
# sa = 'oldBoy'
# s9 = '+'.join(sa)  ##用‘+’号把字符串连接起来
# print(s9)
#
# l1 = ['oldboy','wusir','alex']
# s91=','.join(l1)
# print(s91)

#find 通过元素找索引  找不到返回-1,找到返回1
u = 'odlabced'
u1 = u.find('d')
print(u1)

#字符串格式化输出format
# res='我叫{},今年{}，爱好{}'.format('egon','18','女')
# print(res)
#
# res1='我叫{0}今年{1}岁，爱好{2},我依然叫{0}'.format('egon',18,'male')
# print(res1)
#
# res3='{name} {age} {sex}'.format(sex='male', name='egon', age=18)
# print(res3)

#list
# l = ['老男孩', 'alex', 'wusir', 'taibai', 'ritian']
# l.extend('hu')
# print(l)
# print(l.pop(0))
# l.remove('alex')
# print(l)
# print(l[2])
# l[2]='huningfei'
# print(l)

#元组
tu=(11,2,True,[2,3,4],'alex')
# for i in tu:
#     print(i)

# print (tu[:3:2])
# print(tu.index(True))
# tu[-2].append('99')
# print(tu)

#字典
# dic = {'name': 'taibai', 'age': 21, 'hobby': 'girl', }
# dic['high']=190
# print(dic)
# dic.setdefault('high',180)
# print(dic)
# print(dic.pop('name'))
# print (dic.pop('name1','没有辞职，sb'))
# dic2 = {'name':'alex','weight':75}
# dic2.update(dic)  #将dic所有的键值对覆盖添加（相同的覆盖，没有的添加）到dic2中
# print(dic)
# print(dic2)
#查
# print(dic.get('name'))
# print (dic.get('name1','没有此键值'))
#
# print (list(dic.keys()))#取出键值
# for i in dic.keys():
#     print(i)
#
# print(list(dic.values()))#取出value
# print(list(dic.items()))#同事取出键值和value
# print(len(dic))

dic = {'k1':'v1','k2':'v2','k3':'v3','r':666}
l1 = []
# for i in dic:
#     if 'k' in i:
#         l1.append(i)
# print(l1)
#
# for i in l1:
#     del dic[i]
# print(dic)
