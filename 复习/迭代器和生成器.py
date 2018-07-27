# 这两个都是可迭代的，都会取到1,2,3

# lst_iter = [1,2,3].__iter__()
# print(lst_iter.__next__())
# print(lst_iter.__next__())
# print(lst_iter.__next__())
#
#
# for i in [1,2,3]:
#     print(i)

# print(dir({1,2}))
# print(dir(123))
# print('__next__' in dir(range(12)))
# print(dir(range(12)))
#生成器
# 生成器函数的调用不会触发代码的执行，而是会返回一个生成器(迭代器)
# 想要生成器函数执行，需要用next
#
# def cloth_g(num):
#     for i in range(num):
#         yield 'cloth%s'%i
#
#
# g = cloth_g(1000)
# print(next(g))
# print(next(g))
# print(next(g))


#send
# def generator():
#     print(123)
#     content = yield 1
#     print('=======',content)
#     print(456)
#     yield 2
#
# g = generator()
# ret = g.__next__()
# print('***',ret)#1
# ret = g.send('hello')   #send的效果和next一样
# print('***',ret)

#send 获取下一个值的效果和next基本一致
#只是在获取下一个值的时候，给上一yield的位置传递一个数据
#使用send的注意事项
    # 第一次使用生成器的时候 是用next获取下一个值
    # 最后一个yield不能接受外部的值


print([i**2 for i in range(30) if i%3 ==0])