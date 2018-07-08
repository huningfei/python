import sys
import json
import time

# 学校
class School():
    def __init__(self, school_name):
        self.name = school_name

    def creat_class(self):  # 创建班级
        print("欢迎创建班级".center(50, '-'), '\n')
        classroom_name = input("请输入班级名称: ")
        classroom_period = input("请输入班级周期: ")
        classroom_obj = Clsaaroom(classroom_name, classroom_period)  # 班级类实例
        print("创建班级成功".center(50, '-'), '\n')
        print("班级信息如下:".rjust(10))
        classrooms[classroom_name] = classroom_obj  # 将班级名和班级实例关联起来
        classrooms_dict = {
            "班级名称":classroom_name,
            "班级周期":classroom_period
        }
        classroom_obj.show_classroom_info()
        f = open("班级信息.text",'w')
        f.write(json.dumps(classrooms_dict,ensure_ascii=False, indent=2))#dunps 参数必须要dict类型的
        # dunps输出是二进制格式的   ensure_ascii = False 将输出转换成字符串格式
        #json.dump(classrooms_obj, open("班级信息.text", "w", encoding='utf-8'), ensure_ascii=False, indent=2)
        control_view()  # 从新调用选择功能函数

    def creat_course(self):  # 创建课程
        print("欢迎创建课程:  ".center(50, '-'), '\n')
        course_name = input("请输入课程名称:  ")
        course_period = input("请输入课程周期: ")
        course_pay = input("请输入课程价格: ")
        course_obj = Course(course_name, course_period, course_pay)  # 将课程类实例化
        print("创建课程成功:  ".center(50, '-'), '\n')
        courses[course_name] = course_obj  # 将课程名和课程实例关联起来
        course_dic ={"课程名称":course_name,
                     "课程周期":course_period,
                     "课程价格":course_pay}
        f = open("课程信息",'w')
        f.write(json.dumps(course_dic,ensure_ascii=False,indent=2))
        course_obj.show_course_info()
        control_view()  # 从新调用选择功能函数

    def create_teacher(self):#创建讲师
        print("创建讲师".center(50, '-'))
        teacher_name = input("请输入讲师姓名： ")
        teacher_sex = input("请输入讲师性别： ")
        teacher_age = input("请输入讲师年龄： ")
        teacher_school = input("请输入讲师所在学校： ")
        teacher_course = input("请输入讲师教授课程： ")
        teacher_classroom = input("请输入讲师所在班级： ")
        teacher_obj = Teacher(teacher_name, teacher_age, teacher_sex, teacher_course, teacher_school,
                              teacher_classroom)  # 实例化讲师
        print("创建讲师成功".center(50, '-'))
        teachers[teacher_name] = teacher_obj  # 关联讲师与讲师信息
        teachers_dic= {"讲师姓名":teacher_name,
                       "讲师性别":teacher_sex,
                       "讲师年龄":teacher_age,
                       "讲师所在学校":teacher_school,
                       "讲师教授课程":teacher_course,
                       "讲师所在班级":teacher_classroom}
        teacher_obj.show_teacher_info()
        control_view()#从新调用选择功能函数


# 班级类
class Clsaaroom(object):
    def __init__(self, classroom_name, classroom_period):
        self.classroom_name = classroom_name
        self.classroom_period = classroom_period

    def show_classroom_info(self):
        print("班级名称: %s\n班级周期: %s" % (self.classroom_name, self.classroom_period))

# 课程类 course
class Course(object):
    def __init__(self, course_name, course_period, course_pay):  # period  周期  price 价格
        self.course_name = course_name
        self.course_period = course_period
        self.coyres_pay = course_pay

    def show_course_info(self):
        print("课程名称: %s\n课程周期: %s\n课程价格: %s" % (self.course_name, self.course_period, self.coyres_pay))


# 人员类
class Person(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


# 讲师类
class Teacher(Person):
    def __init__(self, teacher_name, teacher_age, teacher_sex, teacher_course, teacher_school, teacher_classroom):
        super(Teacher, self).__init__(teacher_name, teacher_age, teacher_sex)
        self.teacher_course = teacher_course
        self.teacher_school = teacher_school
        self.teacher_classroom = teacher_classroom

    def show_teacher_info(self):
        print("""
        ——————讲师信息——————
        讲师： %s
        性别： %s
        年龄： %s
        讲师所在学校： %s
        讲师所在班级： %s
        讲师教授课程： %s
        """ % (self.name, self.sex, self.age, self.teacher_course, self.teacher_classroom, self.teacher_school))


# 学生类
class Student(Person):
    def __init__(self, student_name, student_age, student_sex, student_course, student_id, student_period):
        super(Student, self).__init__(student_name, student_age, student_sex)
        self.student_course = student_course
        self.student_id = student_id
        self.student_period = student_period

    def show_student_info(self):
        print("""
           ——————学员信息——————
           讲师： %s
           性别： %s
           年龄： %s
           学生学号： %s
           学生报名课程： %s
           课程周期： %s
           """% (self.name, self.sex, self.age, self.student_id, self.student_course,
                  self.student_period))  # course 课程  period 周期

def Create_stdent():#创建学员
    student_name = input("请输入学生姓名; ")
    student_age  = input("请输入学生年龄: ")
    student_sex  = input("请输入学生性别: ")
    student_id   = input("请输入学生学号: ")
    student_course = input("请输入学生所选课程: ")
    student_period = input("请输入课程周期: ")
    student_obj  = Student(student_name, student_age, student_sex, student_id,student_course,student_period)#实例化学生类
    students[student_name] = student_obj
    students_dict = {"学生姓名":student_name,
                "学生年龄":student_age,
                "学生性别":student_sex,
                "学生学号":student_id,
                "学生所选课程":student_course,
                "课程周期":student_period
                }
    student_obj.show_student_info()
    f = open("学生信息",'a')
    f.write(json.dumps(students_dict,ensure_ascii= False,indent = 2))


def Student_view():
    print("欢迎进入学生视图".center(50,'-'))
    student_choice_id = input("请选择功能： "
          "1.注册"
          "2.缴费"
          "3.选择班级"
          "4.返回"
          "5.退出"
                    )
    if student_choice_id == 1:
        Create_stdent()
    elif student_choice_id == 2:
        pass
    elif student_choice_id == 3:
        pass

def Teacher_view():
    pass

def control_view():#管理视图
    choice_id = input("\n*************************请选择功能********************\n"
                      "1.创建班级"
                      "2.创建课程"
                      "3.创建讲师"
                      "4.返回"
                      "5.退出\n: ")
    #choice_id = int(choice_id)  # input 输入时字符串格式下面的 choice 是int 类型 需要进行类型转换
    if choice_id == '1':
        schoolid.creat_class()
    elif choice_id == '2':
        schoolid.creat_course()
    elif choice_id == '3':
        #print("你好")
        schoolid.create_teacher()
        #print("你好")
    elif choice_id == '4':
        select_fun()
    elif choice_id == '5':
        sys.exit()


def select_school():  # 选择学校
    global schoolid
    choice_school_id = input("\n*************************请选择学校********************\n"
                             "a.北京大学"
                             "b.清华大学"
                             "q.退出\n: ")
    if choice_school_id == 'a':
        schoolid = school1
    elif choice_school_id == 'b':
        schoolid = school2
    elif choice_school_id == 'q':
        sys.exit()
    else:
        print("\033[4;35m请输入真确的选项:\033[0m")


def select_fun():  # 选择功能
    choice_id = input("\n*************************请选择功能********************\n"
                      "1.学院视图"
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
    # schoolid.creat_class()


def main():
    #Create_stdent()
    # print("aaa")

    while True:
        select_school()
        while True:
            select_fun()

if __name__ == '__main__':
    classrooms = {}
    courses = {}
    teachers = {}
    students = {}
    school1 = School("北大")
    school2 = School("清华")

    main()