# python两种类
    # 经典类 py3已经灭绝了 在python2里还存在，在py2中只要程序员不主动继承object，这个类就是经典类   —— 深度优先
    # 新式类 python3所有的类都是新式类，所有的新式类都继承自object —— 在多继承中遵循广度优先算法
# 钻石继承问题
# python3

# class A:
#     def f(self):
#         print('in A')
#
# class B(A):
#     pass
#     # def f(self):
#     #     print('in B')
#
# class C(A):
#     pass
#     # def f(self):
#     #     print('in C')
#
#
# class D(B,C):
#     pass
#     # def f(self):
#     #     print('in D')
#
# class E(C):
#     pass
#     # def f(self):
#     #     print('in B')
#
# class F(D,E):
#     pass
#     # def f(self):
#     #     print('in C')
#
# # d = D()
# # d.f()
#
# print(F.mro())

# class A:
#     def f(self):
#         print('in A')
#
# class B(A):
#     def f(self):
#         print('in B')
#         super().f()
#
# class C(A):
#     pass
#     def f(self):
#         print('in C')
#         super().f()
#
# class D(B,C):
#     def f(self):
#         print('in D')
#         super().f()
#
# d = D()
# d.f()

# super和找父类这件事是两回事
# 在单继承中 super就是找父类
# 在多级承中 super的轨迹 是根据整个模型的起始点而展开的一个广度优先顺序 遵循mro规则
