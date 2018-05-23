import hashlib
# with open('../db/userinfo')as f:
#     print(f.read())

# username='hnf'
# md5obj=hashlib.md5(username.encode('utf-8'))
# md5obj.update('123'.encode('utf-8'))# 使用md5算法的对象来操作字符串里面必须是bytes类型
# ret=md5obj.hexdigest()
# print(ret)
import sys
print(sys.modules[__name__])