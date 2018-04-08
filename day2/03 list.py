l = ['老男孩', 'alex', 'wusir', 'taibai', 'ritian']
# #增
# #append 在组后增加
# l.append('葫芦')
# print (l)
#
# #insert插入
#
# l.insert(1,'bob')  ##在索引是1的地方插入
# print (l)
#
# #迭代添加
#
# l.extend('alex')
# print (l)
# #删除
# #pop 有返回值，按照索引删除
#
# print (l.pop(0))
# print (l)
# #remove
# l.remove('alex')
# print (l)
#
# #clear  清空列表
# # l.clear()
# # print (l)
#
# #del 内存级别删除列表
#
# # del l
# # print (l)
#
# #按索引删除
# # del l[1]
# # print(l)
#
# #切片删除
#
# del l[1:3]
# print (l)

#改
#按照索引去改
# print (l[2])
# l[2]= 'huningfei'
# print (l)
# #按照切片去改
# l[:2] = 'abc'  ##把索引是0和1的全部改成了abc
# print (l)
# l[1:3] = [111,222,333]
# print (l)
# #查询
# #按照索引去查询，按照切片去查下
# for i in l:
#     print (i)
#
# #其他办法
#
a = [8,7,8,3,3,5,3,1,2]
# #count 计数
# print (a.count(8))
#
# #len
# print (len(a))
#
# #sort 从小到大排序
a.sort()
print (a)
a.sort(reverse=True)  ##从大到小
print (a)
b = ['a','b','e','e','g']
#reverse  ##倒过来排序
b.reverse()
print (b)



#联系
# l1 = [1, 2, 'alexdfdf', 'wusir',['oldboy', 'ritian', 10], 'taibai']
# #
# # # l1[2]='ALEX'
# # # print (l1[2])
# # l1[2] = l1[2].upper()
# # print (l1)
#
# l1[-2].append('女神')
# print (l1[-2])
#
# l1[-2][1] = (l1[-2][1].capitalize())
# print (l1)
#
# l1[-2][2]=int(l1[-2][2]) + 90
# print (l1)