import sys
import hashlib
from conf import settings
from core.manager import Manager
from core.student import Student
from core.teacher import Teacher

def login():
    #登录认证,用了动态加盐
    user=input('请输入用户名>>>:')
    pwd=input('请输入密码>>>:')
    hash_obj=hashlib.md5(user.encode('utf-8'))
    hash_obj.update(pwd.encode('utf-8'))
    md5_pwd=hash_obj.hexdigest()
    with open('../db/userinfo') as f:
        for line in f:
            username,passwd,identity=line.strip().split('|')
            if username==user and passwd ==md5_pwd:
                print('\033[1;32m登录成功!\033[0m')

                return {'username':user,'identity':identity} #{'username': 'admin', 'identity': 'Manager'}

def main():
    ret = login()
    if ret: #如果ret不为空

        if hasattr(sys.modules[__name__],ret['identity']):
            Role_cls=getattr(sys.modules[__name__],ret['identity'])
            #print(Role_cls) #<class 'core.manager.Manager'>
            role_obj=Role_cls(ret['username'])
            # print(role_obj)
            while True: #一直循环让用户输入
                if role_obj==Manager:
                    for num,tup in enumerate(role_obj.Operate_lst,1):
                        print(num,tup[0])
                    num=input('请输入你要操作的序号：')
                    func_name = role_obj.Operate_lst[int(num)-1][1] #序号对应的内容
                    if hasattr(role_obj,func_name):
                        getattr(role_obj,func_name)()
                # elif role_obj==Student:
                #     student.student()
