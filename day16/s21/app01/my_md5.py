import hashlib
#动态加盐
def md5(user,pwd):
    md5obj=hashlib.md5(user.encode('utf-8'))
    md5obj.update(pwd.encode('utf-8'))# 使用md5算法的对象来操作字符串里面必须是bytes类型
    return md5obj.hexdigest()



# class Login:
#     def __init__(self, user, password):
#         self.user = user
#         self.password = password
#
#     def md5(self):
#         """
#         md5加密（动态加盐）
#         :return: 密码
#         """
#         md5obj = hashlib.md5(self.user.encode("utf-8"))
#         md5obj.update(self.password.encode("utf-8"))
#         # return md5obj.hexdigest()
#         print(md5obj.hexdigest())
#
#
# user=Login('hu','123')
# # print(user.password)
# user.md5()