# 组合
# 一个类的对象作为另外一个类对象的属性


# class Person:
#     def __init__(self,name,sex,hp,dps):
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
# class Weapon:
#     def __init__(self,name,price,dps):
#         self.name = name
#         self.price = price
#         self.dps = dps
#     def kill(self,dog):
#         dog.hp -= self.dps
#
# alex = Person('alex','N/A',250,5)
# ha2 = Dog('哈士奇','藏獒',15000,200)
# # print(alex.name)
# roubaozi = Weapon('肉包子',600000,10000)
# alex.money = 1000000
# if alex.money >= roubaozi.price:
#     alex.weapon = roubaozi
#     alex.weapon.kill(ha2)
#     print(ha2.hp)
# 基础数据类型 都是类
# 'alex' : str的对象
# alex.name = 'alex'
# alex.name.startswith('a')

#给alex装备一个武器


# 圆形类 --> 圆环类
# 已知圆形类 的基础上 运用组合 求圆环的面积和周长
# 一个类的对象给另一个类对象当属性

# 圆环
# 圆
# 圆环的面积

from math import pi
class Circle:
    def __init__(self,r):
        self.r = r
    def area(self):
        return pi * self.r ** 2
    def perimeter(self):
        return self.r *pi * 2

class Ring:
    def __init__(self,outside_r,inside_r):
        self.out_circle = Circle(outside_r)
        self.in_circle = Circle(inside_r)
    def area(self):
        return self.out_circle.area() - self.in_circle.area()
    def perimeter(self):
        return self.out_circle.perimeter() + self.in_circle.perimeter()

r = Ring(10,5)
print(r.area())
print(r.perimeter())

# 组合 是描述了 一种 什么有什么的关系  圆环有圆   人有武器









