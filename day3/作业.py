#while True:

def login():
    with open('register',encoding='utf-8') as f1:

    ##从register文件中读取验证，三次机会，没成功则结束整个程序

def register():
    with open('register',encoding='utf-8',mode='a+') as f1:
        username = input("请输入你要注册的用户名：")
        passd = input("请输入你的密码：")
        f1.write()
        f1.close()
register()
    #如果register文件里面没有这个用户名则注册成功，并且自动登录成功，否则提示用户名已经存在
@login
def article():
    #如果登录成功才可以访问,否则提示不能访问
@login
def diary():
    #如果登录成功才可以访问,否则提示不能访问
def comment():
    # 如果登录成功才可以访问,否则提示不能访问
def collection():
    #登录成功，才可以查看收藏
def exit():
    #退出登录页面，查看任何页面提示重新登录

dic = {1:'login',
       2:'register',
       3:'article'
       }
