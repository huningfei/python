'''
class 类名:
    静态属性 = 123
    def 动态属性(self):
        # 在类中的方法的一个默认的参数，但也只是一个形式参数,约定必须叫self
        print('-->',self)
print(类名.静态属性)#查看静态属性
类名.静态属性=456
print(类名.静态属性) #修改静态属性
类名.静态属性2='abc' #增加静态属性
print(类名.静态属性2)
del 类名.静态属性2 #删除静态属性

print(类名.动态属性)
类名.动态属性("我要把1传给动态属性self") #这个1传给了self
#print(类名.静态属性2)
'''
#类的第二个功能实例化（创造一个具体的对象）

'''
class Person:pass
alex=Person() #对象=类名() 也叫实例化
print(alex) #对象
print(Person) #类
print(alex.__dict__) #默认是空字典
alex.__dict__['name']='alex' # 给alex对象添加属性
alex.sex='男' #给alex对象添加属性
print(alex.__dict__)
'''

'''
class Person:
    def __init__(self,name,sex,dps,hp):
        self.name=name
        self.sex=sex
        self.dps=dps
        self.hp=hp
    def attack(self,dog): # 人打狗
        dog.hp-=self.dps
        print('%s打了%s,%s还剩%s点血'% (self.name,dog.name,dog.name,dog.hp))

class Dog:

    def __init__(self,name,kind,hp,dps):
        self.name=name
        self.kind=kind
        self.hp=hp
        self.dps=dps
    def bite(self,person):#狗咬人
        person.hp -= self.dps
        print('%s咬了%s,%s还剩%s点血'% (self.name,person.name,person.name,person.hp))

alex = Person('alex','男',250,5)
ha2 = Dog('小白','藏獒',1000,200)
ha2.bite(alex)
#alex.attack(ha2) #第一种写法
# 对象名.方法名 相当于调用一个函数，默认把对象名作为第一个参数传入函数 alex调用了attack函数
Person.attack(alex,ha2)#第二种写法
print(ha2.hp)
'''

#已知半径计算园的面积
# from math import pi
# class Yuan:
#     def __init__(self,r):
#         self.r=r
#     def Yuan_mianji(self):
#
#         return pi *self.r **2
#     def Yuan_zc(self):
#
#         return pi * 2*self.r
# yuan = Yuan(3)
# mj=yuan.Yuan_mianji()
# #mj1=Yuan.Yuan_mianji(yuan)
# zc=yuan.Yuan_zc()
# print('我是面积%s\n我是周长%s'%(mj,zc))

#小练习
# class action:
#     def __init__(self,name,age,sex,zuo):
#         self.name=name
#         self.age=age
#         self.sex=sex
#         self.zuo=zuo
#     def attack(self):
#         print(self.name,self.age,self.sex,self.zuo)
# xm=action('小明,','10岁,','男,','上山去砍柴')
# li=action('老李,','50岁,','男,','开车去东北')
# xm.attack()
# li.attack()

#命名空间
 # 类有自己的命名空间
# 对象也有自己的命名空间
# 对象能访问类的命名空间
# 类不能访问对象的命名空间

class Person:
    COUNTRY = ['中国人']       # 静态属性
    country = '中国人'
    def __init__(self,name):
        self.name = name
    def eat(self):
        print('%s在吃泔水'%self.name)
alex = Person('alex')
egon = Person('egon')
# print(alex.name)
# print(alex.country)
# alex.country='印度人' #这个只是在alex这个对象里面生效
# print(alex.country)
# print(egon.country)
# print(Person.country) # Person里面的没有改过来
# alex.COUNTRY[0] = '印度人' # 如果是列表就整体都改了
# print(alex.COUNTRY)
# print(egon.COUNTRY)
# print(Person.COUNTRY)
alex.COUNTRY=['印度人']
print(egon.COUNTRY) #中国人
print(Person.COUNTRY) #中国人
print(alex.COUNTRY)
'''
#结论
# 在访问变量的时候，都先使用自己命名空间中的，如果自己的空间中没有，再到类的空间中去找
# 在使用对象修改静态变量的过程中，相当于在自己的空间中创建了一个新的变量
# 在类的静态变量的操作中  应该使用类名来直接进行操作 就不会出现乌龙问题

#创建一个类计算创建了多少个实例
# class lei:
#     count = 0
#     def __init__(self):
#         lei.count +=1
# f1=lei()
# 
# print(lei.count)
