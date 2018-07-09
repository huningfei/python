import json
import sys
import time
class School:
    def __init__(self,name):
        self.name=name

    def creat_class(self):
        print('欢迎创建班级'.center(50,'#'),'\n')
        class_name=input("请输入班级名称")
        class_obj=Classroom(class_name)
        print("创建班级成功,信息如下：".center(50, '-'), '\n')
        class_dict = {
            "班级名称": class_name,

        }
        class_obj.show_class()
        f=open('class_info','a')
        f.write(json.dumps(class_dict,ensure_ascii=False))
        control_view()



    def shcool_info(self):
        print('学校名称%s,学校所在地%s'%(self.name,self.name))
class Classroom:
    def __init__(self,class_name):
        self.name=class_name
    def show_class(self):
        print("班级名称是%s"%self.name)






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
                with open('..\作业\db\info',encoding='utf-8')as f1:
                    for i in f1:
                        a = (i.split())
                        if a[0] == username and a[1] == password:
                            print(a[0],a[1])
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

@wrapper
def control_view():#管理视图
    choice_id = input("\n*************************请选择功能********************\n"
                      "1.创建班级"
                      "2.创建课程"
                      "3.创建讲师"
                      "4.返回"
                      "5.退出\n: ")

    if choice_id == '1':
        schoolid.creat_class()
    # elif choice_id == '2':
    #     schoolid.creat_course()
    # elif choice_id == '3':
    #     #print("你好")
    #     schoolid.create_teacher()
    #     #print("你好")
    # elif choice_id == '4':
    #     select_fun()
    # elif choice_id == '5':
    #     sys.exit()
@wrapper
def select_school():
    global schoolid
    choice_school_id = input("\n*************************请选择学校********************\n"
                             "a.北京校区"
                             "b.上海校区"
                             "q.退出\n: ")
    if choice_school_id == 'a':
        schoolid = school1
    elif choice_school_id == 'b':
        schoolid = school2
    elif choice_school_id == 'q':
        sys.exit()
    else:
        print("\033[4;35m请输入真确的选项:\033[0m")
@wrapper
def select_fun():  # 选择功能
    choice_id = input("\n*************************请选择功能********************\n"
                      "1.学员视图"
                      "2.讲师视图"
                      "3.管理视图"
                      "4.返回\n: ")
    # choice_id = int(choice_id)  #input 输入时字符串格式下面的 choice 是int 类型 需要进行类型转换
    if choice_id == '1':
        print("待完善")
    elif choice_id == '2':
        print("待完善")
    elif choice_id == '3':
        control_view()
        # print("你好11111")
    elif choice_id == '4':
        select_school()
    else:
        return
    time.sleep(2)

def main():
    while True:
        select_school() #选择功能#
        select_fun() #选择学校



if __name__ == '__main__':
    classrooms = {}

    # teachers = {}
    # students = {}
    school1 = School('昌平校区')
    school2 = School('浦东校区')


    main()


# dic = {1:login,
#
#
#        }

# def chiose():
#     global school1
#     global school2
#     while True:
#         school1=School('昌平')
#         school2=School('浦东')
#         global login
#         with open('..\作业\db\shcool-mange',encoding='utf-8') as f1:
#               print(f1.read())
#               num= int(input("请选择一个序号操作：").strip())
#               if num == 1:
#                   dic.get(num)()
#                   #login()
#               elif num ==3:
#                   schoolid.creat_class()
#
#
#
# chiose()
