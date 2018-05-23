#from core.manager import Foo

class Foo:
    def __repr__(self):
        show_str=''
        for key in self.__dict__:
            show_str+='%s:%s'%(key,self.__dict__[key])
        return show_str

class Student(Foo):
    def __init__(self,name):
        self.name=name