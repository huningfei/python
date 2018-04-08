
#赋值运算，它们共用一个列表
# a = [1,2,3]
# b = a
# a.append(666)
# print(a,b)

#浅copy
#对于浅copy来说，第一层创建的是新的内存地址，而从第二层开始，
# 指向的都是同一个内存地址，所以，对于第二层以及更深的层数来说，保持一致性
l1 = [1,2,3]
l2 = l1.copy()
l1.append(666)
print(l1,l2)
print(id(l1),id(l2))

l1 = [1,2,3,[22,33]]  ##这里因为[22,33]属于第二层，所以两个列表都一样
l2 = l1.copy()
l1[-1].append(666)
print(l1,l2)
print(id(l1[-1]),id(l2[-1]))

#深copy 对于深copy来说，两个是完全独立的，改变任意一个的任何元素（无论多少层），另一个绝对不改变。
import copy
l1 = [1,2,3,[22,33]]
l2 = copy.deepcopy(l1)
l1[-1].append(666)
print(l1,l2)
print(id(l1[-1]),id(l2[-1]))
#
# id == is
a = 'alex'
b = 'alex'
print(a == b)  # 数值
print(a is b)  # 内存地址
print(id(a))

#python中 有小数据池的概念。
# int -5 ~256 的相同的数全都指向一个内存地址，节省空间。
# str：s = 'a' * 20 以内都是同一个内存地址
    #只要字符串含有非字母元素，那就不是一个内存地址

    