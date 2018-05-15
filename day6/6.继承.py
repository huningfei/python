# 为什么会有继承？  解决代码的冗余问题
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

# class Parent:pass
# class Son(Parent):pass
# 单继承
# Son类 继承 Parent类
# 父类 基类 超类  —— Parent类
# 子类 派生类 —— Son类

# 多继承
# class Parent1:pass
# class Parent2:pass
#
# class Son(Parent1,Parent2):pass
# class Animal:
#     def __init__(self, name, hp, dps):
#         self.name = name
#         self.hp = hp
#         self.dps = dps
#     def eat(self):
#         print('%s吃药回血了'%self.name)
# class Person(Animal):
#     def __init__(self, name, hp, dps,sex):
#         super().__init__(name,hp,dps)    # Animal.__init__(self,name,hp,dps)
#         self.sex = sex           # 派生属性
#     def attack(self,dog):
#         dog.hp -= self.dps
#         print('%s打了%s,%s掉了%s点血,剩余%s点血' % (self.name, dog.name, dog.name, self.dps, dog.hp))
#
# class Dog(Animal):
#     def __init__(self,name,hp,dps,kind):
#         super().__init__(name, hp, dps)   # Animal.__init__(self, name, hp, dps)
#         self.kind = kind         # 派生属性
#     def bite(self,person):
#         person.hp -= self.dps
#         print('%s打了%s,%s掉了%s点血,剩余%s点血' % (self.name, person.name, person.name, self.dps, person.hp))
# alex = Person('alex',250,5,'N/A')
# ha2 = Dog('哈士奇',15000,200,'藏獒')
# print(alex.__dict__)
# print(ha2.__dict__)
# ha2.eat()
# alex.eat()
# ha2.bite(alex)
# alex.attack(ha2)
# 对象的内存空间 - 创建这个对象的类的内存空间 - 父类的

# class Foo:
#     def __init__(self):
#         self.func()
#     def func(self):
#         print('in Foo')
#
# class Son(Foo):
#     def func(self):
#         print('in Son')
# Son()
