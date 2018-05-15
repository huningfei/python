# 昵称，name
# sex，sex
# 战斗力，dps
# 血液，hp
'''
class Person:
    def __init__(self,name,sex,hp,dps):
        self.name=name
        self.sex=sex
        self.hp=hp
        self.dps=dps
    def attack(self,dog): #人打狗
        dog.hp-=self.dps
        print('%s打了%s,%s掉了%s点血，还剩%s点血' %(self.name,dog.name,dog.name,self.dps,dog.hp))
class Dog:
    def __init__(self, name, kind, hp, dps):
        self.name = name
        self.kind=kind
        self.hp = hp
        self.dps = dps
    def bitt(self,person): #狗咬人
        person.hp -= self.dps
        print('%s咬了%s,%s掉了%s点血，还剩%s点血' % (self.name, person.name, person.name, self.dps, person.hp))

class Weapon:
    def __init__(self,name,price,dps):
        self.name=name
        self.price=price
        self.dps=dps
    def kill(self,dog):
        dog.hp -= self.dps

alex =Person('alex','男',250,5)
ha2 = Dog('小黑','藏獒',10000,200)
roubaozi = Weapon('肉包子',500000,1000) #实例化武器
alex.money=1000000
if alex.money >= roubaozi.price:
    alex.weapon = roubaozi #一个类的对象给另外一个类的对象当属性，就是roubaozi给alex这个对象当属性
    alex.weapon.kill(ha2) #这是组合的常见方式  对象点属性是一个新的对象就是roubaozi
    print('小黑还剩%s点血'%(ha2.hp))

alex.attack(ha2)
ha2.bitt(alex)
'''
##计算园环面积和周长,圆环面积=大圆面积-小圆面积  圆环周长=大环周长+小环周长
from math import pi
class Yuan:
    def __init__(self,r): #4
        self.r=r
    def mj(self):
        return pi*self.r**2
    def zc(self):
        return 2*pi*self.r

class huan:
    def __init__(self,outside_r,inside_r): #2
        self.outside=Yuan(outside_r) #大圆半径 #3
        self.inside=Yuan(inside_r)  #小圆半径 #4
    def huan_mj(self):
        return self.outside.mj()-self.inside.mj() #5
    def huan_zc(self):
        return self.outside.zc()-self.inside.zc()
r=huan(10,5)  #1
print(r.huan_mj())
print(r.huan_zc())
# yuan=Yuan(4)
# mj=yuan.mj()
# zc=yuan.zc()
# print(mj,zc)
