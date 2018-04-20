##博客地址：http://www.cnblogs.com/huningfei/p/8849749.html  文件
##http://www.cnblogs.com/huningfei/p/8849968.html  函数

##存贮用户登录状态的
user_status = {
    'username': None,
    'status': False
}
##登录函数
def wrapper(f2):
    def inner():
        if user_status.get('status'):
            f2()  ##就是被装饰的函数
        else:
            # login()
            print('注意，请先登录，在操作，超过三次锁定用户')
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
                            return username
                    else:
                        print("登录失败，请重新登录,你已经用了%s次" % (b+1))
                    b += 1
    return inner
@wrapper
def login(): ##这里重新定义一个login函数，因为你如果直接执行装饰器会报错，因为里面传了一个参数
    pass

def register(): ##注册
    flag = True
    while True:
        with open('register', encoding='utf-8', mode='r') as f1,\
                open('register', encoding='utf-8', mode='a') as f2:
            username = input("请输入你要注册的用户名：").strip()
            if not username.isalnum() or not username.isdigit():
                pass
            else:
                print("用户名不能只有数字，请更改")
                continue
            for i in f1:
                if username in i:
                    print("用户名已经存在，请更改")
                    break
            else:
                while flag:
                    one_passwd = input("请输入你的密码：").strip()
                    two_passwd = input("请再次输入你的密码:").strip()
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
@wrapper # article = login(article)
def article():
       with open('article',encoding='utf-8') as f1:

           print(f1.read())


@wrapper
def diary():
    print('\033[1;33m-----欢迎来到日记页面-----\033[0m')

@wrapper
def comment():
    print('-----欢迎来到评论页面------')
@wrapper
def collection():
    print('------欢迎来到收藏页面------')
@wrapper
def logout():
    user_status['status'] = False
    print("你已经退出")
@wrapper
def quit():
    print("你已退出整个程序")
    exit()

dic = {1:login,
       2:register,
       3:article,
       4:diary,
       5:comment,
       6:collection,
       7:logout,
       8:quit
       }

##输出提示内容
while True:
    with open('zuoye',encoding='utf-8') as f1:
          print(f1.read())
          a = int(input("请选择一个序号操作：").strip())
          dic.get(a)()

