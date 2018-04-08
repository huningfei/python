tu = (11,2,True,[2,3,4],'alex')
#查找
for i in tu:
    print (i)

#切片
print (tu[1])
print (tu[:3:2])

print(tu.index(True))
#count 统计
print(tu.count(2))
#len长度
print(len(tu))
#添加
tu[-2].append('99')
print (tu)