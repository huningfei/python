import hashlib
#动态加盐
def md5(user,pwd):
    md5obj=hashlib.md5(user.encode('utf-8'))
    md5obj.update(pwd.encode('utf-8'))# 使用md5算法的对象来操作字符串里面必须是bytes类型
    return md5obj.hexdigest()



