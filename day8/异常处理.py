# s1 = 'hello'
# try:
#     int(s1)
# except ValueError as e:
#     print(e)
#多分枝
# s1 = 'hello'
# try:
#     int(s1)
# except IndexError as e:
#     print(e)
# except KeyError as e:
#     print(e)
# except ValueError as e:
#     print(e)
#万能异常
#
# # s1 = 'hello'
# try:
#     int(s1)
# except Exception as e:
#     print(e)

# try:
#     f=open('a','w')
#     l=[1]
#     num=int(input('num:'))
#     l[num]
# except ValueError:print('请输入一个数字')
# except IndexError:print('你要找的项目不存在')
# except Exception as e:print(e)
# else:print('执行elses')# 如果try语句中的代码都顺利的执行了，没有报错，那么执行else中的代码
# finally:  ##(无论如何都会执行finally)
#     print('执行了finally')
#     f.close()

#重用的处理异常结构
# try:
#     pass #可能有问题的代码
# except ValueError:  # 能预料到的错误
#     pass
# except Exception as e:print(e) # 能处理错有的异常
# else:pass          # try中的代码没有错误的时候执行
# finally:pass

#主动触发异常
# try:
#     raise TypeError('类型错误')
# except Exception as e:
#     print(e)

#断言 assert
assert 1==1
print('ok')
# assert 1==2
# print('error')


