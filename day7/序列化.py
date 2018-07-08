# 什么叫序列化呢？
    # { '10100011':{'name':,age: ,class:},}
    # 数据类型 —— 字符串的过程
# 什么时候要用序列化呢？
    # 数据从内存到文件
    # 数据在网络上传输  字节 - 字符串 - 字典
# python中的序列化模块都有哪些？
    # json   通用的 支持的数据类型 list tuple dict
    # pickle python中通用的 支持几乎所有python中的数据类型
    # shelve python中使用的便捷的序列化工具


'''
#json
#dumps和loads是和内存交互的
#dump和load是和文件交互的
import json
dic={'k':'v'}
# print(type(dic))
# json_dic=json.dumps(dic) # 字典转字符串的过程 ——序列化
# print(json_dic)
# print(dic)
# print(type(json_dic))
# print(json.loads(json_dic))  #字符串 转回其他数据类型 —— 反序列化

#注意可以dump多次，但是不能多次load
# with open('d','w')as f:
#     json.dump(dic,f) #和文件交互
#
# with open('d')as f:
#     print(json.load(f))
#怎样dump多条数据
# 如果要dump多条数据
# 每一条数据先dumps一下 编程字符串 然后打开文件 write写进文件里 \n
# 读取的时候按照标志读取或者按行读
# 读出来之后 再使用loads

with open('aaa','w')as f:
    str_dic=json.dumps(dic)
    f.write(str_dic+'\n')
    f.write(str_dic + '\n')
    f.write(str_dic + '\n')
with open('aaa')as f:
    for line in f:
        print(json.loads(line.strip()))
'''

#pickle
import pickle
class A:
    def __init__(self,name):
        self.name=name
alex=A('alex')
print(pickle.dumps(alex))

with open('b_pickle','wb')as f:
    pickle.dump(alex,f)
    pickle.dump(alex, f)
with open('b_pickle','rb')as f:
    while True:
        try:
            obj=pickle.load(f)
            print(obj.name)
        except EOFError:
            break
#注意
#1.pickle支持更多的数据类型
# 2.pickle的结果是二进制
# 3.pickle在和文件交互的时候可以被多次load