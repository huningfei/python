class Foo:
    def __repr__(self):
        show_str=''
        for key in self.__dict__:
            show_str+='%s:%s'%(key,self.__dict__[key])
        return show_str

class Student(Foo):
    def __init__(self,name):
        self.name=name

def student():
    Operate_lst = [('查看自己的班级', 'show_courses'),
                   ('查看自己的课程', 'create_class'),
                   ]