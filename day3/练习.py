# 1. 文件a.txt内容：每一行内容分别为商品名字，价钱，个数。
# apple 10 3
# tesla 100000 1
# mac 3000 2
# lenovo 30000 3
# chicken 10 3
# 通过代码，将其构建成这种数据类型：[{'name':'apple','price':10,'amount':3},{'name':'tesla','price':1000000,'amount':1}......] 并计算出总价钱。

#new_list=[]
# total = 0
# with open('article',encoding='utf-8') as f1:
#     for i in f1:
#         a=(i.split())
#         # print(a)
#         new_list.append({'name':a[0],'price':a[1],'amount':a[2]})
# print(new_list)
# f1.close()
# for g in new_list:
#     money = g['price']
#     count = g['amount']
#     total = total + int(money) * int(count)
# print(total)

##第二种写法，别人的
# product = []
# file = open("article")
# flag = True
# total = 0
# while flag:
#     line = file.readline().strip()
#     if not line:
#         flag = False
#         break
#     temp = line.split()
#     p = {"name": '', 'price': 0, 'amount': 0}
#     p['name'] = temp[0]
#     p['price'] = int(temp[1])
#     p['amount'] = int(temp[2])
#     total = total + p.get('price') * p.get('amount')
#     product.append(p)
#
# file.close()
# print(product)
# print(total)

# 2，有如下文件：
# -------
# alex是老男孩python发起人，创建人。
# alex其实是人妖。
# 谁说alex是sb？
# 你们真逗，alex再牛逼，也掩饰不住资深屌丝的气质。
# ----------
# 将文件中所有的alex都替换成大写的SB。
# import os
# with open('2.txt',encoding='utf-8') as f1,\
#     open('2.txt.bak',encoding='utf-8',mode='w') as f2:
#     for line in f1:
#         new_line = line.replace('alex','SB')
#         f2.write(new_line)
# os.remove('2.txt')
# os.rename('2.txt.bak','2.txt')


# 2、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
# new_list=[]
# jishu = []
# def func1(*args):
#     return 111,22,3,4,5,7,87
# ret = func1()
# new_list.extend(ret)
# #print(new_list[0])
# for i in range(len(new_list)):
#     if i%2 != 0:
#         jishu.append(new_list[i])
#     else:
#         pass
# print(jishu)

# ret1=[]
# with open('2.txt',encoding='utf-8') as f1:
#     li = f1.readline().split()
#     print(li)
#     for i in f1:
#         dic = {}
#         #print(i)
#         for j in range(len(li)):
#             dic[li[j]] = i.split()[j]
#         ret1.append(dic)
# print(ret1)

##推导式
# list = []
# with open('2.txt',encoding='utf-8') as f1:
#     keys = [i for i in f1.readline().split()]
#     #print(keys)
#     for volumes in f1:
#         print(volumes)
#         list.append({k:v for k,v in zip(keys,volumes.split())})
#     print(list)
##注册
# user_status = {
#     'username': None,
#     'status': False
# }
# def register():
#     flag = True
#     while True:
#         with open('register', encoding='utf-8', mode='r') as f1,\
#                 open('register', encoding='utf-8', mode='a') as f2:
#             username = input("请输入你要注册的用户名：")
#             for i in f1:
#                 if username in i:
#                     print("用户名已经存在，请更改")
#                     break
#             else:
#                 while flag:
#                     one_passwd = input("请输入你的密码：")
#                     two_passwd = input("请再次输入你的密码:")
#                     if one_passwd != two_passwd:
#                         print("你的密码不一致，请重新输入")
#                         continue
#                     else:
#                         f2.write('%s  %s\n' % (username, two_passwd))
#                         user_status['status'] = True
#                         if user_status.get('status'):
#                             print("你已经注册并登陆成功")
#                         flag = False
#
#                 break
#         f1.close()
#         f2.close()
# register()
# ##登录
#
#
# def login():
#     print('注意，超过三次锁定用户')
#     b = 0
#     while b < 3:
#         username = input("请输入你的用户名：")
#         password = input("请输入你的密码:")
#         with open('register',encoding='utf-8')as f1:
#             for i in f1:
#                 a = (i.split())
#                 if a[0] == username and a[1] == password:
#                     user_status['status'] = True
#                     print(user_status.get('status'))
#                     print("登录成功")
#                     exit()
#             else:
#                 print("登录失败，请重新登录,你已经用了%s次" % (b+1))
#             b += 1
# login()


##装饰
# def wrapper(f1):
#     def inner(*args,**kwargs):
#         if user_status.get('status')  ##如果登录成功，则正常访问
#             ret = f1(*args,**kwargs)
#             return ret
#         else:
#             login()
#     return f1
# wrapper()



def comment():
    with open('article',encoding='utf-8') as f1:
        wen = f1.read()
        print(wen)

comment()



