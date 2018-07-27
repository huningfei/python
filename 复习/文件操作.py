#r+读写
# with open('log1',encoding='utf-8',mode='r+')as f1:
#     f1.seek(0,2)###把光标调整到最后，然后再去写，原来的内容不会被覆盖
#     # print(f1.read())
#     f1.write('555')
#     f1.seek(0)##然后把光标调整到最前面，再去读
#     print(f1.read())

#w写
# with open('log1',encoding='utf-8',mode='w+') as f1:
#     f1.write('哈哈哈')
#     f1.seek(0)
#     print(f1.read())

#a追加和a+可写，可读
# with open('log1',encoding='utf-8',mode='a') as f1:
#     f1.write('\n很好')
#     f1.seek(0)
#     # print(f1.read())
#
# with open('log1',encoding='utf-8',mode='a+') as f1:
#     f1.write('\n很好莫今天是')
#     f1.seek(0)
#     print(f1.read())
#文件的改
# import os
# with open('log1',encoding='utf-8') as f1,\
#     open('log1.bak',encoding='utf-8',mode='w+') as f2: #f1打开源文件，f2创建新文件
#     for line in f1:
#         new_line=line.replace('hahaha','dfdf')#要改变的内容
#         f2.write(new_line)#写入到新文件
#         f2.seek(0)
#         print(f2.read())
# os.remove('log1')
# os.rename('log1.bak','log1')

#tell指针
# with open('log2',encoding='utf-8',mode='a+')as f1:
#     f1.write('dfdfdfdfdfdf')
#     print(f1.tell())

#编码转换
# s1 = b'\xd6\xd0\xb9\xfa'
# s2 = s1.decode('gbk')
# print(s2)
# s3 = s2.encode('utf-8')
# print(s3)

#练习
# 通过代码，将其构建成这种数据类型：[{'name':'apple','price':10,'amount':3},
# {'name':'tesla','price':1000000,'amount':1}......] 并计算出总价钱
new_list=[]
total = 0
with open('log1',encoding='utf-8',mode='r') as f1:
    for i in f1:
        a=(i.split())
        new_list.append({'name':a[0],'price':a[1],'amount':a[2]})
print(new_list)



for g in new_list:
    money = g['price']
    count = g['amount']
    total = total + int(money) * int(count)
print(total)