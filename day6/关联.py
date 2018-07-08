# from math import pi
# class Cricle:
#     def __init__(self,r):
#         self.r=r
#     @property
#     def area(self):
#         return self.r ** 2 *pi
#     def perimeter(self):
#         return  self.r *2 * pi
# c=Cricle(3)
# # print(c.area())
# print(c.area)
# print(c.perimeter())

#计算房间的面积
class Room:
    def __init__(self,chang,kuan,gao):
        self.chang=chang
        self.kuan=kuan
        self.gao=gao
    def area(self):
        return self.chang*self.kuan*self.gao
a = Room(2,3,4)
print(a.area())