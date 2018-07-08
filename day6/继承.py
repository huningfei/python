# 继承概念  继承是一种创建新类的方式，在python中，新建的类可以继承一个或多个父类，父类又可称为基类或超类，新建的类称为派生类或子类
'''
class Animal:
    def __init__(self,name,dps,hp):
        self.name=name
        self.dps=dps
        self.hp=hp
    def eat(self):
        print('%s吃药,回血了'%(self.name))
class Person(Animal):
    def __init__(self,name,dps,hp,sex):
        super().__init__(name,dps,hp)   #第二中写法  Animal.__init__(self,name,dps,hp)

        self.sex=sex
    def attack(self,dog):
        dog.hp -= self.dps
        print('%s打了%s,%s掉了%s点血，%s还剩%s点血'%(self.name,dog.name,dog.name,self.dps,dog.name,dog.hp))

class Dog(Animal):
    def __init__(self,name,dps,hp,kind):
        super().__init__(name,dps,hp)
        self.kind=kind
    def bite(self,person):
        person.hp -= self.dps
        print('%s咬了%s,%s掉了%s点血，%s还剩%s点血' % (self.name, person.name, person.name, self.dps, person.name, person.hp))
alex=Person('alex',5,250,'男')
ha2=Dog('小黑',200,2000,'藏獒')
print(alex.__dict__)
print(ha2.__dict__)
alex.attack(ha2)
ha2.bite(alex)
ha2.eat()
'''
#寻找init方法的步骤
#先找对象的内存空间 - 创建这个对象的类的内存空间（子类） - 父类的内存空间

#面试题
class Foo:
    def __init__(self):
        self.func()
    def func(self):
        print('in Foo')

class Son(Foo):

    def func(self):
        print('in Son')
Son()
#实例化了一个对象，找自己方法里面的self，然后再去执行父类里面的self，然后又去调用func,所以打印in son