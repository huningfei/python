'''


def person(name,sex,hp,dps):
    dic = {'name':name,'sex':sex,'hp':hp,'dps':dps,'bag':[]}
    def attack(dog):
        dog['hp'] -= dic['dps']
        print('%s打了%s,%s掉了%s点血，还剩%s血'%(dic['name'],dog['name'],dog['name'],dic['dps'],dog['hp']))
    dic['attack'] =attack # 把attack函数加入到dic里面
    #print('dic',dic)
    return dic

def dog(name,kind,hp,dps):
    dic = {'name':name,'kind':kind,'hp':hp,'dps':dps}
    def bite(person):
        person['hp'] -= dic['dps']
        print('%s打了%s,%s掉了%s点血，还剩%s血'%(dic['name'],person['name'],person['name'],dic['dps'],person['hp']))
    dic['bite'] = bite
    return dic

alex=person('alex','nan',250,5) #alex 接收到了person函数即第一个dic
ha2=dog('小黑','藏獒',13000,200) # ha2接收到了dog函数即第二个dic
print(alex)
#print(ha2)
print(alex['attack']) #内部函数
print(alex['attack'](ha2))
# print(ha2)

'''


# class Person():
#     def __init__(self,name,sex,hp,dps):
#         self.name=name
#         self.sex=sex
#         self.hp = hp
#         self.dps =dps
# alex = Person('alex','男',259,5)
# print(alex.__dict__)
# print(alex.name)

###
# class Person:pass
# alex = Person()
#
# print(alex)  # object
# print(alex.__dict__) ##默认是空字典
# alex.name = 'alex'   # 给alex对象添加属性
# alex.hp = 250
# alex.dps = 5
# alex.sex = '不详'
# alex.bag = []
# print(alex.__dict__)
# print(Person) #类
#
'''

class Person():
    def __init__(self,name,hp,dps,sex):
        self.name=name
        self.hp=hp
        self.dps=dps
        self.sex=sex
        self.bag=[]
    def attack(self,dog):
        dog.hp -=self.dps
        print('%s打了%s,%s掉了%s点血，还剩%s血' % (self.name, dog.name, dog.name, self.dps, dog.hp))

class Dog():
    def __init__(self,name,hp,dps,sex):
        self.name=name
        self.hp=hp
        self.dps=dps
        self.sex=sex
        self.bag=[]
    def attack(self,dog):
        dog.hp -=self.dps
        print('%s打了%s,%s掉了%s点血，还剩%s血' % (self.name, dog.name, dog.name, self.dps, dog.hp))


alex = Person('alex','男',259,5)
ha2=Dog('小黑','藏獒',13000,200)
alex.attack()
'''
##园的面积和周长
# from math import pi
# class Yuan():
#     def __init__(self,r):
#         self.r=r
#     def yuan_mianji(self):
#         return pi * self.r ** 2
#     def yuan_zc(self):
#         return 2*pi*self.r
# r=Yuan(3)
# print(r.yuan_mianji())
# print(r.yuan_zc())

# class Person():
#     COUNTRY = ['中国人']
#     def __init__(self,name):
#         self.name=name
#     def eat(self):
#         print('%s在吃泔水'%self.name)
# alex=Person('alex')
# egon=Person('egon')
# print(alex.COUNTRY) #中国人
# alex.COUNTRY=['印度人']
# print(alex.COUNTRY) #印度人
# print(egon.COUNTRY) #中国人
# Person.COUNTRY=['泰国人']
# print(egon.COUNTRY)
# print(alex.COUNTRY)


class Person:
    role = 'person'
    def __init__(self,name):
        self.name=name
    def walk(self):
        print('person is walking')
print(Person.role)
print(Person.walk)
egg=Person('egon')
print(egg.name)
print(egg.walk())
