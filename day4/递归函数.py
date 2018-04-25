# def func():
#     print(1)
#     func()
#
# func()    # 997 /998

# import sys
# def foo(n):
#     print(n)
#     n += 1
#     foo(n)
# foo(1)

# 6!
# print(6*5*4*3*2*1)
def fn(n):
    if n == 1: return 1
    return n * fn(n - 1)


print(fn(6))

# 递归 就是自己调用自己
# 递归需要有一个停止的条件
# def fn(6):
#     if 6 == 1:return 1
#     return 6*fn(5)
# print(fn(6))
#
# def fn(5):
#     return 5*fn(4)
#
# def fn(4):
#     return 4*fn(3)
#
# def fn(3):
#     return 3*fn(2)
#
# def fn(2):
#     return 2*fn(1)
#
# def fn(1):
#     return 1