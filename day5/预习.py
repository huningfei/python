##json模块
import json
# #dumps  将字典转换成字符串
# dic ={'k1':'1','k2':'2'}
# str=json.dumps(dic)
# print(str)
#
# list_dic = [1,['a','b','c'],3,{'k1':'v1','k2':'v2'}]
# print(json.dumps(list_dic))
# #loads 将字符串转换成字典
# dic1=json.loads(str)
# print(type(dic1))

##dump #dump方法接收一个文件句柄，直接将字典转换成json字符串写入文件
# f = open('json_file','w')
# dic = {'k1':'v1','k2':'v2','k3':'v3'}
# json.dump(dic,f)
# f.close()

#load#load方法接收一个文件句柄，直接将文件中的json字符串转换成数据结构返回
# f = open('json_file')
# dic2 = json.load(f)
# f.close()
# print(type(dic2),dic2)

##pickle 用于python特有的类型 和 python的数据类型间进行转换

import pickle
#dumps
# dic = {'k1':'v1','k2':'v2','k3':'v3'}
# str_dic = pickle.dumps(dic)
# print(str_dic) ##返回二进制内容
# #loads
# dic2 = pickle.loads(str_dic)
# print(dic2) #返回字典

import time
# struct_time=time.localtime(1000000000)
# print(struct_time)
# f = open('pickle_file','wb')
# pickle.dump(struct_time,f)
# f.close()

f = open('pickle_file','rb')
struct_time2 = pickle.load(f)
print(struct_time2.tm_year)