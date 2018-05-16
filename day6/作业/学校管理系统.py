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
import json
import sys
import time
class School: #学校类
    def __init__(self,name):
        self.name=name

    def creat_class(self): #创建班级
        print('欢迎创建班级'.center(50,'#'),'\n')
        class_name=input("请输入班级名称")
        class_obj=Classroom(class_name)
        print("创建班级成功,信息如下：".center(50, '-'), '\n')
        class_dict = {
            "班级名称": class_name,
        }

        if schoolid == school1:

            f=open('bj_class_info','a')
            f.write(json.dumps(class_dict,ensure_ascii=False))
            control_view()
        else:
            f = open('sh_class_info', 'a')
            f.write(json.dumps(class_dict, ensure_ascii=False))
            control_view()

    def show_class(self):#查看班级
        if schoolid == school1:
            f=open('bj_class_info','r')
            print(f.read())
        else:
            f = open('sh_class_info', 'r')
            print(f.read())

    def creat_course(self): # 创建课程
        print('欢迎创建课程'.center(50, '#'), '\n')
        course_name=input("请输入课程名称")
        course_time=input("请输入课程周期")
        course_price=input("请输入课程价格")
        course_obj=Course(course_name,course_time,course_price)
        print("创建课程成功：" '\n')
        courses[course_name]=course_obj
        course_dict ={"课程名称":course_name,
              "课程周期":course_time,
              "课程价格":course_price
        }
        if schoolid == school1:
            f = open('bj_course_info', 'a')
            f.write(json.dumps(course_dict, ensure_ascii=False)+'\n')
            control_view()
        else:
            f = open('sh_course_info', 'a')
            f.write(json.dumps(course_dict, ensure_ascii=False)+'\n')
            control_view()
    def show_course(self): #查看课程
        if schoolid == school1:
            f = open('bj_course_info', 'r')
            print(f.read())

        else:
            f = open('sh_course_info', 'r')
            print(f.read())


    def create_teacher(self):
        print("创建讲师".center(50,'#'))
        teacher_name=input("请输入讲师姓名:")
        teacher_sex=input("请输入讲师性别:")
        teacher_age=input("请输入讲师年龄:")
        teacher_school=input("请输入讲师所在学校:")
        teacher_class=input("请输入讲师所在班级:")
        teacher_course=input("请输入讲师教授的课程:")
        teacher_obj=(teacher_name,teacher_sex,teacher_age,teacher_school,teacher_class,teacher_course)
        print("创建讲师成功：".center(50, '-'), '\n')
        teachers[teacher_name] = teacher_obj
        teachers_dic={
            "讲师姓名": teacher_name,
            "讲师性别": teacher_sex,
            "讲师年龄": teacher_age,
            "讲师所在学校": teacher_school,
            "讲师教授课程": teacher_course,
            "讲师所在班级": teacher_class

        }
        if schoolid == school1:
            f = open('bj_teacher_info', 'a')
            f.write(json.dumps(teachers_dic, ensure_ascii=False))
            control_view()
        else:
            f = open('sh_teacher_info', 'a')
            f.write(json.dumps(teachers_dic, ensure_ascii=False))
            control_view()
    def show_teacher(self): #查看讲师
        if schoolid == school1:
            f = open('bj_teacher_info', 'r')
            print(f.read())
        else:
            f = open('sh_teacher_info', 'r')
            print(f.read())









class Classroom: #班级类
    def __init__(self,class_name):
        self.name=class_name
class Course: #课程类
    def __init__(self,course_name,course_time,course_price):
        self.course_name=course_name
        self.course_time=course_time
        self.course_price=course_price
class Person:
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age
class Teacher(Person):
    def __init__(self,teacher_name,teacher_sex,teacher_age,teacher_school,teacher_class,teacher_course):
        super(Teacher,self).__init__(teacher_name,teacher_sex,teacher_age)
        self.teacher_school=teacher_school
        self.teacher_course=teacher_course
        self.teacher_age=teacher_age





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
            print('\033[1;33m欢迎来到教学管理系统.\033[0m'.center(50,"#"),"\n")
            print('\033[1;33m注意，请先登录，再操作，超过三次锁定用户\033[0m')
            b = 0
            while b < 3:
                username = input("\033[1;33m请输入你的用户名:\033[0m")
                password = input("\033[1;33m请输入你的密码:\033[0m")
                with open('db\info',encoding='utf-8')as f1:
                    for i in f1:
                        a = (i.split())
                        if a[0] == username and a[1] == password and a[2] == 'student':
                            user_status['status'] = True

                            print("\033[1;33m登录成功\033[0m")
                            #main()
                            student_view()
                            return username
                        elif a[0] == username and a[1] == password and a[2] == 'teacher':
                            user_status['status'] = True

                            print("\033[1;33m登录成功\033[0m")
                            #main()
                            teacher_view()
                            return username
                        elif a[0] == username and a[1] == password and a[2] == 'manage':
                            user_status['status'] = True

                            print("\033[1;33m登录成功\033[0m")
                            #main()
                            control_view()
                            return username

                    else:
                        print("登录失败，请重新登录,你已经用了%s次" % (b+1))
                    b += 1
    return inner
@wrapper
def login(): ##这里重新定义一个login函数，因为你如果直接执行装饰器会报错，因为里面传了一个参数
    pass

#@wrapper
def control_view():#管理视图

    choice_id = input("\n*************************请选择功能********************\n"
                      "0.查看班级"
                      "1.创建班级"
                      "2.创建课程"
                      "3.查看课程"
                      "4.创建讲师"
                      "5.查看讲师"
                      "6.返回"
                      "7.退出\n: ")
    if choice_id =='0':
        schoolid.show_class()
    if choice_id == '1':
        schoolid.creat_class()
    elif choice_id == '2':
        schoolid.creat_course()
    elif choice_id == '3':
        schoolid.show_course()
    elif choice_id == "4":
        schoolid.create_teacher()
    elif choice_id == '5':
        schoolid.show_teacher()

    elif choice_id == '6':
        select_fun()
    elif choice_id == '7':
        sys.exit()
def student_view(): #学生视图
    choice_id = input("\n*************************学生功能********************\n"
                      "0.查看班级"
                      "1.查看课程")

    if choice_id =='0':
        schoolid.show_class()
    elif choice_id == '1':
        schoolid.show_course()
def teacher_view(): #老师视图
    choice_id = input("\n*************************讲师功能********************\n"
                      "0.查看班级"
                      "1.查看课程"
                      "2.退出\n: ")
    if choice_id == '0':
        schoolid.show_class()
    elif choice_id == '1':
        schoolid.show_course()
    elif choice_id =='2':
        sys.exit()

#@wrapper
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
#@wrapper
def select_fun():  # 选择功能
    global choice_id
    choice_id = input("\n*************************请选择角色********************\n"
                      "1.学员视图"
                      "2.讲师视图"
                      "3.管理视图"
                      "4.返回\n: ")
    # choice_id = int(choice_id)  #input 输入时字符串格式下面的 choice 是int 类型 需要进行类型转换
    if choice_id == '1':
        student_view()

    elif choice_id == '2':
        teacher_view()

    elif choice_id == '3':
        control_view()
        # print("你好11111")
    elif choice_id == '4':
        select_school()
    # else:
    #     return
    #time.sleep(2)

#@wrapper
def main():
    while True:
        select_school() #选择学校
        while True:
            login() #选择功能



if __name__ == '__main__':
    classrooms = {}
    teachers = {}
    courses = {}
    students = {}
    school1 = School('昌平校区')
    school2 = School('浦东校区')


    main()




