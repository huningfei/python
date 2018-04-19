##存贮用户登录状态的
user_status = {
    'username': None,
    'status': False
}
## 序号对应函数




def login():  ## ##从register文件中读取验证，三次机会，没成功则结束整个程序
    print('注意，超过三次锁定用户')
    b = 0
    while b < 3:
        username = input("请输入你的用户名：")
        password = input("请输入你的密码:")
        with open('register',encoding='utf-8')as f1:
            for i in f1:
                a = (i.split())
                if a[0] == username and a[1] == password:
                    user_status['status'] = True
                    print(user_status.get('status'))
                    print("登录成功")
                    exit()
            else:
                print("登录失败，请重新登录,你已经用了%s次" % (b+1))
            b += 1
# login()


def register(): ##注册
    flag = True
    while True:
        with open('register', encoding='utf-8', mode='r') as f1,\
                open('register', encoding='utf-8', mode='a') as f2:
            username = input("请输入你要注册的用户名：")
            for i in f1:
                if username in i:
                    print("用户名已经存在，请更改")
                    break
            else:
                while flag:
                    one_passwd = input("请输入你的密码：")
                    two_passwd = input("请再次输入你的密码:")
                    if one_passwd != two_passwd:
                        print("你的密码不一致，请重新输入")
                        continue
                    else:
                        f2.write('%s  %s\n' % (username, two_passwd))
                        user_status['status'] = True
                        if user_status.get('status'):
                            print("你已经注册并登陆成功")
                        flag = False

                break
        f1.close()
        f2.close()
# register()

#@login
def article():
       with open('a.txt',encoding='utf-8') as f1:
              f1.read()
    #如果登录成功才可以访问,否则提示不能访问
# article()
#
# @login
# def diary():
#     #如果登录成功才可以访问,否则提示不能访问
# def comment():
#     # 如果登录成功才可以访问,否则提示不能访问
# def collection():
#     #登录成功，才可以查看收藏
# def exit():
#     #退出登录页面，查看任何页面提示重新登录
#
dic = {1:login,
       2:register,
       3:article
       }

b = dic.get(2)
b()
##输出提示内容
# with open('zuoye',encoding='utf-8') as f1:
#        print(f1.read())
#        a = int(input("请选择一个序号操作：").strip())
#        b = dic.get(a)
#        print(b)