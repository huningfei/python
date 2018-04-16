#


# with open('log1',encoding='utf-8',mode='r') as f1:
#     print(f1.read())
#     f1.close()
# f1 = open('log1',encoding='utf-8',mode='r+')
# f1.seek(0,2)   ##把光标调整到最后，然后再去写，原来的内容不会被覆盖
# f1.write('aaaaaaaaaaaa')
# f1.seek(0) ##然后把光标调整到最前面，再去读
# print(f1.read())
# f1.close()

# f1 = open('log1',encoding='utf-8',mode='w')
# f1.write('我们都是好孩子')
# f1.close()

# f1 = open('log1',mode='wb')  ##默认是bytes类型，然后转换成utf-8写入到log1文件中
# f1.write('我们都是好孩子'.encode('utf-8'))
# f1.close()


##追加 a
# f1 = open('log1',encoding='utf-8',mode='a')
# f1.write('ddddddddddd')
# f1.close()

#可写可读a+
# f1 = open('log1',encoding='utf-8',mode='a+')
# f1.write('999999')
# f1.seek(0)
# print(f1.read())
# f1.close()

##文件的改

# import os
# with open('log1',encoding='utf-8') as f1,\
#     open('log1.bak',encoding='utf-8',mode='w') as f2:
#     for line in f1:
#         new_line = line.replace('99','dd')
#         f2.write(new_line)   ##把替换完成的内容，写到f2里面
#
# os.remove('log1')
# os.rename('log1.bak','log1')

#read(n)
# f1 = open('log1',encoding='utf-8')
# print(f1.read(5))
# f1.close()
#
# f2 = open('log1',mode='rb')
# print(f2.read(6).decode('utf-8'))
# f2.close()

#readlines
f1 = open('log1',encoding='utf-8',)
print(f1.readlines())
f1.close()

f2 = open('log1',encoding='utf-8',mode='w')
f2.write("aaaaaaaaaaaaa")
print(f2.tell())
f2.close()
