import pickle
import os
import hashlib
from conf import settings
from core.teacher import Teacher
from core.student import Student
from core import mypickle

class Foo:
    def __repr__(self):
        show_str=''
        for key in self.__dict__:
            show_str+='%s:%s'%(key,self.__dict__[key])
        return show_str
class School(Foo):
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr
class Classes(Foo): #班级类
    def __init__(self,name,course):
        self.name=name
        self.course=course


class Manager:
    Operate_lst = [('创建学校', 'create_school'),
                   ('创建课程', 'create_courses'),
                   ('创建班级', 'create_classes'),
                   ('创建学员账号', 'create_student'),
                   ('创建讲师账号', 'create_teacher'),
                   ('查看学校', 'show_school'),
                   ('查看讲师', 'show_teacher'),
                   ('查看班级', 'show_class'),
                   ('查看课程', 'show_course'),
                   ('查看学生', 'show_student'),
                   ('给课程关联讲师', 'combine_teacher_course'),
                   ('给学员指定班级', 'add_student'),
                   ('退出', 'quit')
                         ]
    def __init__(self,name):
        self.name=name
        self.school_pickle=mypickle.MyPickle(settings.school_info)
        self.teacher_pickle = mypickle.MyPickle(settings.teacher_info)
        self.class_pickle = mypickle.MyPickle(settings.class_info)
        self.student_pickle = mypickle.MyPickle(settings.student_info)

    def create_school(self):
        sch_name=input('请输入学校名字：')
        sch_addr=input('请输入学校地址: ')
        sch_obj=School(sch_name+',',sch_addr)
        self.school_pickle.dump(sch_obj)
        print('创建学校成功')

    def show_school(self):

        for num,school_obj in enumerate(self.school_pickle.load(),1):

            print( '\033[1;32m查看学校:%s,%s\033[0m'% (num,school_obj))
    def create_classes(self):
        class_name=input("请输入班级名称：")
        course=input('请输入课程：')
        clas_obj = Classes(class_name+',',course) #实例化班级
        self.class_pickle.dump(clas_obj)#存储班级对象的信息到 classinfo 文件里
    def show_class(self):
        for num,class_obj in enumerate(self.class_pickle.load(),1):
            print('\033[1;32m查看班级:%s,%s\033[0m' % (num, class_obj))

    def __register(self,identity):#创建用户的方法
        username=input('请输入要创建的%s角色的姓名' %identity)
        passwd=input('请输入密码')
        md5_obj=hashlib.md5(username.encode('utf-8'))
        md5_obj.update(passwd.encode('utf-8'))
        md5_passwd=md5_obj.hexdigest()
        new_user_info='%s,|%s,|%s\n' % (username,md5_passwd,identity)
        with open(settings.userinfo,mode='a',encoding='utf-8') as f:
            f.write(new_user_info)
        return username

    def create_courses(self):
        pass
    def create_teacher(self):
        username=self.__register('Teacher')
        #给老师选一个校区
        self.show_school()
        school_num=int(input('请输入老师所在的学校序号：'))
        school_obj=self.school_pickle.get_item(school_num) #根据序号活动了一个学校名字
        teacher_obj=Teacher(username+',')
        teacher_obj.school=school_obj # 将老师选择的校区和老师对象绑定在一起
        self.teacher_pickle.dump(teacher_obj) # 将老师对象整体dump进入teacherinfo文件
        print('创建老师成功')

    def show_teacher(self):
        for num, teacher_obj in enumerate(self.teacher_pickle.load(), 1):
            print('\033[1;32m查看信息为:%s,%s\033[0m' % (num, teacher_obj))

    def create_student(self):
        username=self.__register('Student')
        self.show_class() #查看有哪些班级
        cls_num=int(input('请选择要绑定的班级')) #把班级对象绑定给学生
        cls_obj=self.class_pickle.get_item(cls_num) #根据cla_num去判断班级是否存在
        # 创建一个学员对象,把学员的信息写在studentinfo
        stu_obj=Student(username+',')
        stu_obj.class_obj=cls_obj
        self.student_pickle.dump(stu_obj)
    def show_student(self):
        for num, student_obj in enumerate(self.student_pickle.load(), 1):
            print('\033[1;32m查看信息为:%s,%s\033[0m' % (num, student_obj))


