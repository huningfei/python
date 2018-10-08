class Foo:
    f = '类的静态变量'
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say_hi(self):
        print('hi,%s'%self.name)

obj=Foo('egon',73)
print(obj.__dict__,type(obj))

#检测是否含有某属性
print(hasattr(obj,'name'))
print(hasattr(obj,'say_hi'))

#获取属性
n=getattr(obj,'name')
print(n)
func=getattr(obj,'say_hi')
func()

print(getattr(obj,'aaaaaaaa','不存在啊')) #报错

#设置属性
setattr(obj,'sb',True)
setattr(obj,'age','88')
setattr(obj,'show_name',lambda self:self.name+'sb')
print(obj.__dict__)
# print(obj.show_name(obj))

# #删除属性
# delattr(obj,'age')
# delattr(obj,'show_name')
# delattr(obj,'show_name111')#不存在,则报错
#
# print(obj.__dict__)
