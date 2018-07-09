#hashlib模块  摘要算法  --->  单向不可逆 用于加密
# 包含了多种算法
# 将一个字符串进行摘要运算 拿到不变的 固定长度的值
import hashlib
md5obj=hashlib.md5() # 实例化一个md5摘要算法的对象
md5obj.update('alex3714'.encode('utf-8')) # 使用md5算法的对象来操作字符串
ret = md5obj.hexdigest() #获取算法的结果 hex+digest 16进制+消化
print(ret,type(ret))

#加盐
md5obj=hashlib.md5('hello'.encode('utf-8')) # 实例化一个md5摘要算法的对象，加盐
md5obj.update('alex3714'.encode('utf-8'))# 使用md5算法的对象来操作字符串
ret=md5obj.hexdigest()
print(ret)

#动态加盐
username='hu'
md5obj=hashlib.md5(username.encode('utf-8'))
md5obj.update('alex3714'.encode('utf-8'))# 使用md5算法的对象来操作字符串里面必须是bytes类型
ret=md5obj.hexdigest()
print(ret)


class Longin:
    def __init__(self,name,passwd):
        self.name=name
        self.passwd=passwd

    def hamd5(self):
        name = input('<<<:')
        pwd = input('<<<:')
        md5obj = hashlib.md5(self.name.encode('utf-8'))
        md5obj.update('self.passwd'.encode('utf-8'))
        ret=md5obj.hexdigest()
        print(ret)
    # @staticmethod
    # def login():


alex=Longin('alex','alex3714')
alex.hamd5()

