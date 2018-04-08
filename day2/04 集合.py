set1 = {1,'alex',False,(1,2,3)}
#集合外面是大括号，但是没有冒号，字典也是大括号，有冒号
#元组是()括号，列表是[]


#增
# set1.add('bb')
# print (set1)
# #删除
# set1.pop()  ##括号里面不用写东西，是随机删除一个元素的
# print (set1)
#
# set1.clear()  ##清空列表
# print (set1)

# del set1  ##删除集合
# print (set1)

set3 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
#交集 &
print (set3 & set2)

#并集 |   union
print (set3 | set2)

#差集  -  difference
print (set3 - set2)
print (set2 - set3)

#反交集 ^ symmetric_difference  就是打印双方都没有的元素

print (set2 ^ set3)

set4 = {1,2,3}
set5 = {1,2,3,4,5,6}

print (set4 < set5)  ##返会true  说明set1是set2子集。
print(set4.issubset(set5))

print(set5 > set4)

#frozenset  返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
s = frozenset('barry')
s1 = frozenset({4,5,6,7,8})
print(s,type(s))
print(s1,type(s1))


