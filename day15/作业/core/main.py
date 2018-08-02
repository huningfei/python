from core import register
from core import login

# 选择功能函数
def choice():
    print("""请选择功能：1注册，2登录""")
    while True:
        num = input("请选择你要的功能序号：").strip()
        if num == "1":
            register.register()
            break
        elif num == "2":
            login.login()
            break
        else:
            print('你输入的不符合要求')
            continue
choice()
