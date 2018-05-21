'''
# property的用法
#第一种写法：
from math import pi
class Circle:
    def __init__(self,r):
        self.r=r
    def mj(self):
        return pi*self.r**2
    def zc(self):
        return 2*pi*self.r
c1=Circle(3)
print(c1.mj())

#第二种写法：用property 将一个函数伪装成为属性
class Circle:
    def __init__(self,r):
        self.r=r
    @property
    def mj(self):
        return pi*self.r**2
    @property
    def zc(self):
        return 2*pi*self.r
c1=Circle(3)
print(c1.mj)


# property 跟__私有属性的结合 如：苹果打折的问题
class Goods():
    def __init__(self,price,discount):
        self.__price=price
        self.discount=discount
    @property
    def price(self): #现有的价格
        return self.__price * self.discount
    @price.setter #设置一个新的属性即新的价格
    def price(self,newprice):
        self.__price=newprice
    @price.deleter #删除一个价格
    def price(self):
        del self.__price

apple=Goods(8,0.7)
print(apple.price)
apple.price=10
print(apple.price)
print(apple.__dict__)
del apple.price
print(apple.__dict__)
'''


# classmethod
class Person:
    Country='中国人'
    @classmethod  #把func变成了一个类方法
    def func(cls): #cls指向了类的内存空间
        print('当前角色的国家是%s' %cls.Country)
alex=Person()
alex.func()

Person.func()
#如果某一个类中的方法 并没有用到这个类的实例中的具体属性
# 只是用到了类中的静态变量 就使用类方法