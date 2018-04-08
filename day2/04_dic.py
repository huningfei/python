dic = {'name': 'taibai', 'age': 21, 'hobby': 'girl', }
#
# #增加
#
# dic ['high'] = 180  ##有则覆盖，无则添加
# print (dic)
# dic ['name'] = 'ritian'
# print (dic)
#
# dic.setdefault('high',170) ##有则不变，无责添加
# print (dic)
# dic.setdefault('sex','nan')
# print (dic)
#
# #删除
# print (dic.pop('name'))
# print (dic.pop('name1','没有辞职，sb'))
#
# # dic.clear() #清空
# # print (dic)
#
# print (dic.popitem()) #随机删除，返回值
# #改
# dic['name'] = 'laonanhai'
# print (dic)
#
# dic2 = {'name':'alex','weight':75}
# dic2.update(dic)
# print (dic)
# print (dic2)

#查

# print (dic['name'])
# print (dic.get('name'))
# print (dic.get('name1','没有此键值'))


# #keys() values() items()
# print (list(dic.keys()))  ##可以取出键值，变成列表
# for i in dic.keys():  ##可以循环打印键值
#     print (i)
#
#
# print (list(dic.values()))   ##只能取出values
# for i in dic.values():
#     print (i)
#
# print (list(dic.items()))  ##可以同时取出键值和values
# for i in dic.items():
#     print (i)

##其他类型
#分别赋值
a,b = 1,2
print (a,b)
a = 1
b = 5
print (a,b)

for k,v in dic.items():
    print (k,v)

#len 长度

print (len(dic))

##fromkeys  创建一个新字典

dic1 = dict.fromkeys('abc', '张三')
print (dic1)

#打印结果  {'a': '张三', 'b': '张三', 'c': '张三'}
dic3 = dict.fromkeys('abc',[10])
print (dic3)

dic3['a'].append('oldboy')
print (dic3)
#打印结果      {'a': ['oldboy'], 'b': ['oldboy'], 'c': ['oldboy']}











# dic = {
#     'name_list':['b哥', '张帝', '人帅', 'kitty'],
#     '老男孩':{
#         'name':'老男孩',
#         'age': 46,
#         'sex': 'ladyboy',
#     },
# }
#
# a = (dic['name_list'])
# b=(dic['name_list']).append('骑兵')

