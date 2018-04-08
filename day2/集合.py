'''
集合：
    无序，不重复的数据类型。它里面的元素必须是可哈希的。但是集合本身是不可哈希的。
    1：关系测试。交集并集，子集，差集....
    2,去重。（列表的去重）
'''

l1 = [1,1,2,2,3,3,4,5,6,6]  ##去除重复
l2 = list(set(l1))
print(l2)

#增
set1 = {'alex','wusir','ritian','egon','barry'}

set1.add('999')
print (set1)

set1.update('abc')
print (set1)

#打印结果是'alex', 'ritian', 'b', '999', 'a', 'c', 'egon', 'barry', 'wusir'}

#删
#remove
set1.remove('egon')
print (set1)

# #pop
# set1.pop()  ##随机删除不能指定
# print (set1)

#clear
set1.clear()
print (set1)