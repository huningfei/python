l1 = ['alex', 'wusir', 'taibai', 'barry', '老男孩']
#1
# del l1[1::2]
# print(l1)
#
# for i in range(len(l1)):
#     print(l1)  # ['alex', 'wusir', 'taibai', 'barry', '老男孩']
#                 # ['alex', 'wusir', 'taibai', 'barry', '老男孩']
#                 # ['alex', 'taibai', 'barry', '老男孩']
#                  # ['alex', 'taibai', 'barry', '老男孩']
#     print(i) # 0 1  2  3
#     if i % 2 == 1:
#         del l1[i]
#     print(l1) # ['alex', 'wusir', 'taibai', 'barry', '老男孩']
#              # ['alex', 'taibai', 'barry', '老男孩']
#             # ['alex', 'taibai', 'barry']
#     print(i) # 0 1
#再循环一个列表时，不要对列表进行删除的动作(改变列表元素的个数动作)，会出错

#range 可定制的数字列表
# for i in range(10):
#     print(i)
# for i in range(1,10):
#     print(i)
# for i in range(1,10,2):
#     print(i)

# for i in range(10,1,-1):
#     print(i)
# print(range(10))
# for i in range(len(l1)-1,-1,-1):
#     if i % 2 == 1:
#         del l1[i]
# print(l1)

# dict 再循环字典时，不要改变字典的大小。
# dic = {'k1':'v1','k2':'v2','k3':'v3','r':666}
# l1 = []
# for i in dic:
#     if 'k' in i:
#         l1.append(i)
# # print(l1)
#
# for i in l1:
#     del dic[i]
# print(dic)

#tu 如果元组里面只有一个元素并且没有逗号隔开，那么他的数据类型与该元素一致。
# tu1 = (1)
# print(tu1,type(tu1))
# tu2 = ('alex')
# print(tu2,type(tu2))
#
# tu3 = (['alex',1,2])
# print(tu3,type(tu3))