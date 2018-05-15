# 类  ： 具有相同属性和相同动作的一类事物 组成一个类,如人类
# 对象 ： 具体的某一个具有实际属性 和具体动作的一个实体。如蜘蛛侠就是一个对象

# 类是抽象的
# 对象是具体的
# 类被创造出来 就是模子 是用来描述对象的

# class 类名:
#     静态属性 = 123
#     def 动态属性(self):
#         # 在类中的方法的一个默认的参数，但也只是一个形式参数,约定必须叫self
#         print('-->',self)
#
# # 只要是写在类名中的名字 不管是变量还是函数名 都不能在类的外部直接调用
# # 只能通过类名来使用它
# # 类名的第一个功能是 —— 查看静态属性
# print(类名.静态属性)   # 查看
# 类名.静态属性 = 456    # 修改
# print(类名.静态属性)
# 类名.静态属性2 = 'abc'# 增加
# print(类名.静态属性2)
# # del 类名.静态属性2
# # print(类名.静态属性2)
# print(类名.__dict__)   # 类中必要的默认值之外 还记录了程序员在类中定义的所有名字

# 类名可以查看某个方法，但是一般情况下 我们不直接使用类名来调用方法
# print(类名.动态属性)
# 类名.动态属性(1)


# 类的第二个功能是 —— 实例化（创造对象）
# class Person:pass
#
# alex = Person()
# 对象 = 类名()
# print(alex)  # object
# print(Person)
# alex name hp dps bag sex
# print(alex.__dict__)
# # alex.__dict__['name'] = 'alex'
# # alex.__dict__['sex'] = '不详'
# # alex.__dict__['hp'] = 250
# # alex.__dict__['dps'] = 5
# # alex.__dict__['bag'] = []
# # print(alex.__dict__)
# alex.name = 'alex'   # 给alex对象添加属性
# alex.hp = 250
# alex.dps = 5
# alex.sex = '不详'
# alex.bag = []
# print(alex.__dict__)

# class Person:
#     def __init__(self,name,hp,dps,sex):
#         self.name = name
#         self.hp = hp
#         self.dps = dps
#         self.sex = sex
#         self.bag = []
#
# alex = Person('alex',250,5,'N/A')
# print('alex : ',alex)
# print(alex.__dict__)
# print(alex.name)
# 为什么会执行init中的内容？
# self到底是什么？
# 实例化的过程
# 类名()就是实例化
# 在实例化的过程中 发生了很多事情是外部看不到的
# 1.创建了一个对象
# 2.自动调用__init__方法
# 这个被创造的对象会被当做实际参数传到__init__方法中，并且传给第一个参数self
# 3.执行init方法中的内容
# 4.自动的把self作为返回值 返回给实例化的地方

# class Person:
#     def __init__(self,name,hp,dps,sex):
#         self.name = name
#         self.hp = hp
#         self.dps = dps
#         self.sex = sex
#         self.bag = []
#     def attack(self,dog):
#         dog.hp -= self.dps
#         print('%s打了%s,%s掉了%s点血,剩余%s点血' % (self.name, dog.name, dog.name, self.dps, dog.hp))
#
# class Dog:
#     def __init__(self,name,kind,hp,dps):
#         self.name = name
#         self.hp = hp
#         self.dps = dps
#         self.kind = kind
#
#     def bite(self,person):
#         person.hp -= self.dps
#         print('%s打了%s,%s掉了%s点血,剩余%s点血' % (self.name, person.name, person.name, self.dps, person.hp))
#
# alex = Person('alex',250,5,'N/A')
# ha2 = Dog('哈士奇','藏獒',15000,200)
# ha2.bite(alex)

# 简化的方式
# alex.attack(ha2)   # Person.attack(alex)
# alex.attack(ha2)   # Person.attack(alex)
# print(alex.attack(ha2))   # Person.attack(alex)
# print(ha2.hp)
# print('alex : ',alex)
# print(alex.__dict__)
# print(alex.name)

# 对象名.方法名 相当于调用一个函数，默认把对象名作为第一个参数传入函数
# 剩余的其他参数根据我的需求可以随意传

# 已知半径 计算圆形的面积和周长 面向对象的思想完成
# 类 圆
# 属性 半径
# 方法 计算面积 计算周长 计算直径
# pi * r ** 2
# 2*pi*r
# from math import pi
# class Circle:
#     def __init__(self,r):
#         self.r = r
#     def area(self):
#         return pi * self.r ** 2
#     def perimeter(self):
#         return self.r *pi * 2
#     def r2(self):pass
# c1 = Circle(5)

# 圆形的周长和面积
# 正方形的周长和面积
#
# 每一个角色都有属于自己的 属性 和 方法
# 高可扩展性  可读性  规范性
# 结局不可控

# 类有自己的命名空间
# 对象也有自己的命名空间
# 对象能访问类的命名空间？
# 类不能访问对象的命名空间？
# class Person:
#     COUNTRY = '中国人'       # 静态属性
#     def __init__(self,name):
#         self.name = name
#     def eat(self):
#         print('%s在吃泔水'%self.name)
#
# alex = Person('alex')
# egon = Person('egon')
#
# print(alex.name)
# print(egon.name)
# print(alex.COUNTRY)
# alex.eat()   # Person.eat(alex)
# alex ---> Person
# 当一个类在创建一个实例的时候 就产生了一个这个实例和类之间的联系
# 可以通过实例 对象 找到实例化它的类
# 但是 类不能找到它的实例化


class Person:
    COUNTRY = ['中国人']       # 静态属性
    Country = '中国人'         # 静态属性
    def __init__(self,name):
        self.name = name
    def eat(self):
        print('%s在吃泔水'%self.name)
alex = Person('alex')
egon = Person('egon')
# print(alex.Country)
# alex.Country = '印度人'
# print(alex.Country)
# print(egon.Country)
# print(Person.Country)
# alex.COUNTRY[0] = '印度人'
# print(alex.COUNTRY)
# print(egon.COUNTRY)
# print(Person.COUNTRY)
# alex.COUNTRY = ['印度人']
# print(egon.COUNTRY)
# print(Person.COUNTRY)
# 在访问变量的时候，都先使用自己命名空间中的，如果自己的空间中没有，再到类的空间中去找
# 在使用对象修改静态变量的过程中，相当于在自己的空间中创建了一个新的变量
# 在类的静态变量的操作中  应该使用类名来直接进行操作 就不会出现乌龙问题

# 创建一个类 能够自动计算这个类有创建了多少个实例
# class Foo:
#     count = 0
#     def __init__(self):
#         Foo.count += 1
#
# f1 = Foo()
# print(Foo.count)
# [Foo() for i in range(10)]
# print(Foo.count)