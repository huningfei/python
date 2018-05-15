# import pickle
#
# obj = ('北京','昌平沙河')
#
# # 序列化到文件
# with open("file","wb")as f:
#     pickle.dump(obj,f)
# f.close()
#
#
# #读取文件
# df = open('file','rb')
# read = pickle.load(df)
# df.close()

import json
f=open('file','w')
a={'name':'北京','place':'昌平沙河'}
json.loads(a,f,ensure_ascii=False)
# ret = json.dumps(a,ensure_ascii=False)
# print(ret)