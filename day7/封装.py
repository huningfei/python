# class Person():
#     __country='中国'
#     print(__country)
# print(Person.__dict__)
# print(Person._Person__country) # 不能使用这种方式去调用私有的变量
# #私有的名字，只能在类的内部使用，不能在类的外部使用
# Person.__name='XXX' #在类的外部不能定义私有变量
# print(Person.__name)
# print(Person.__dict__)


#私有变量：
# 在类的内部 如果使用__变量的形式会发生变形，python会自动的为你加上_类名
# class Person():
#     __country='中国' #私有的静态属性
#     def __init__(self,name,pwd):
#         self.name=name
#         self.__pwd=pwd #私有的对象属性
#     def login(self):
#         print(self.__dict__)
#         if self.name=='alex' and self.__pwd=='alex3714':
#             print('登录成功')
# alex=Person('alex','alex3714')
# alex.login()
# print(alex.__dict__)

# class Persion():
#     def __init__(self):pass
#     def __制造密码转换(self): #私有方法
#         print('转换成功')
#     def 注册(self):
#         inp = input('pwd>>>')
#         加密之后的密码=self.__制造密码转换(inp)
# alex=Persion()
# alex.注册()


# 静态属性 、 对象属性、 方法（动态属性） 前面加上双下划綫都会变成私有的
# 私有的特点就是只能在类的内部调用，不能在类的外部使用


#面试题：
class Foo:
    def __init__(self):
        self.func()
    def func(self):
        print('in FOO')
class Son(Foo):
    # def __init__(self):
    #     self.func()
    def func(self):
        print('in son')
s=Son()

#2
class Foo:
    def __init__(self):
        self.__func()
    def __func(self):
        print('in foo')
class Son(Foo):
    def __func(self):
        print('in son')
s=Son()