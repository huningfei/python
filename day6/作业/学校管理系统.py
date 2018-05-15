#https://gitee.com/ygqygq2/python_homework/tree/master/day6%E4%BD%9C%E4%B8%9A
import pickle
'''

import json
class School:
    def __init__(self,name,place):
        self.name=name
        self.place=place
    def create(self):
        dic={"name":self.name,"place":self.place}
        str=json.loads(dic)
        print(type(str))
        # with open('file',encoding='utf-8',mode='a') as f1:
        #     print(self.name)
        #     f1.write(str)



        #print('创建了%s校区，地址在%s'%(self.name,self.place))


    # def beijing(self):
    #     在北京-属性
    #
    # def shanghai(self):
    #     地点在上海-属性
beijing=School('北京','昌平沙河')
beijing.create()


# class 学员
#     选择学校-方法
#     选择班级-方法
#
#
#
# class 课程
#     linux方法 在北京开
#     周期和价格
#     go   方法 在上海开
#     周期和价格
#     python 方法 在北京开
#     周期和价格
# class 讲师
#     关联学校
#
# class 登录
#     学员登录-方法
#     讲师登录-方法
#     管理员登录-方法
'''
##存贮用户登录状态的
user_status = {
    'username': None,
    'status': False
}
##登录函数
def wrapper(f2):
    def inner():
        func1 = str(inner)
        func2 = str(quit)
        if func2 in func1:
            exit()
        if user_status.get('status'):
            f2()  ##就是被装饰的函数
        else:
            print('\033[1;33m注意，请先登录，在操作，超过三次锁定用户\033[0m')
            b = 0
            while b < 3:
                username = input("\033[1;33m请输入你的用户名:\033[0m")
                password = input("\033[1;33m请输入你的密码:\033[0m")
                with open('db/school-mange',encoding='utf-8')as f1:
                    for i in f1:
                        a = (i.split())
                        if a[0] == username and a[1] == password:
                            user_status['status'] = True
                            print("\033[1;33m登录成功\033[0m")
                            return username
                    else:
                        print("登录失败，请重新登录,你已经用了%s次" % (b+1))
                    b += 1
    return inner
@wrapper
def login(): ##这里重新定义一个login函数，因为你如果直接执行装饰器会报错，因为里面传了一个参数
    pass
dic = {0:login,

       }
while True:

    with open('db/school-mange',encoding='utf-8') as f1:
          print(f1.read())
          num= int(input("请选择一个序号操作：").strip())
          dic.get(num)()



