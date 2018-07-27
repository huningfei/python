#浅copy
# 对于浅copy来说，第一层创建的是新的内存地址，而从第二层开始，指向的都是同一个内存地址，所以，对于第二层以及更深的层数来说，
# 保持一致性。
# l1 = [1,2,3,['barry','alex']]
# l2=l1.copy()
# # print(l2)
# print(l1,id(l1)) #[1, 2, 3, ['barry', 'alex']] 2916415390600
# print(l2,id(l2)) #[1, 2, 3, ['barry', 'alex']] 2916416395912
# l1[1]=222
# print(l1,id(l1))#[1, 222, 3, ['barry', 'alex']] 2916415390600 l1的值改变了，而l2的值没有变
# print(l2,id(l2)) #[1, 2, 3, ['barry', 'alex']] 2916416395912

# l1[3][0]='wusir'  #l1和l2的值是一样的。
# print(l1,id(l1[3]))#[1, 2, 3, ['wusir', 'alex']] 2654134573768
# print(l2,id(l2[3]))#[1, 2, 3, ['wusir', 'alex']] 2654134573768

#深拷贝deepcopy
# 对于深copy来说，两个是完全独立的，改变任意一个的任何元素（无论多少层），另一个绝对不改变。
# import copy
# l1 = [1,2,3,['barry','alex']]
# l2 = copy.deepcopy(l1)
# print(l1,id(l1))
# print(l2,id(l2))

# l1[1]=222
# print(l1,id(l1))
# print(l2,id(l2))

# l1[3][0] = 'wusir'
# print(l1,id(l1[3]))
# print(l2,id(l2[3]))


#小数据池
#python中 有小数据池的概念。
 # int -5 ~256 的相同的数全都指向一个内存地址，节省空间。
 # str：s = 'a' * 20 以内都是同一个内存地址
a=5
b=5
print(type(a))
print(id(a))#1406758496
print(id(b))#1406758496
print(a is b )

user1='12'
user2='12'
print(id(user1)) #2675065969552
print(id(user2))#2675065969552


