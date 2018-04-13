
# name = input ('请输入你的姓名：')
# sex = input ('请输入你的性别：')
# print ('我的名字是' +name ,'我的性别是' +sex)


# a = '你好，'
# b = '朋友'
# c = a + b
# print(c)

# name = input('请输入你的名字：')
# age = input('请输入你的年龄：')
# job = input('请输入你的工作：')
# hobby = input('请输入你的爱好：')
# msg1 = ''' ------------ info of %s -----------
# Name  : %s
# Age   : %d
# job   : %s
# Hobbie: %s
# ------------- end -----------------
# ''' % (name,name,int(age),job,hobby)
# print(msg1)

# #1 一个条件
# if 2 > 1 :
#     print(666)
#
#
# #2 一个条件两种结果
# if 2 < 1:
#     print(666)
# else:
#     print(555)
#
# #3 多种条件选一个结果
# num = int(input('猜一下数字：'))
# if num == 6:
#     print('请你吃饭')
# elif num == 3:
#     print('请你喝酒')
# elif num == 1:
#     print('请你唱歌')
# #4 多种条件必选一个结果
# num = int(input('猜一下数字：'))
# if num == 6:
#     print('请你吃饭')
# elif num == 3:
#     print('请你喝酒')
# elif num == 1:
#     print('请你唱歌')
# else:
#     print('没机会了.....')

# while True:
#     print('凉凉')
#     print('黄昏')
#     print('我有一个道姑朋友')

#打印1到100，当小于等于100的时候可以一直打印，否则就退出
# count = 1
# while count <= 100:
#     print(count)
#     count = count + 1
##打印1到100的数字之和
# count = 0
# sum = 1
# while count <101:
#
#     sum=sum+count
#     count += 1
#
# print (sum)




# while True:
#     print(333)
#     print(5455)
#     print(222)
#     break
#     print(888)
# print(666)

# while True:
#     print(333)
#     print(5455)
#     print(222)
#     continue
#     print(888)
# print(666)

# count = 1
# while count < 5:
#     print(count)
#     count += 1
# else:
#     print('循环正常完毕')

# s = 'fdsanmnxfdfd'
# for i in s:
#     if i == 'a':pass
#     print(i)
# else:
#     print(666)

#练习

#使用while循环输入 1 2 3 4 5 6     8 9 10
# i = 0
# while i <10:
#
#     i+=1
#     if i ==7:
#         continue
#
#
#     print (i)

#输出 1-100 内的所有偶数
# i = 0
# while i<101:
#     if i%2==0:
#         print (i)
#     i+=1

#输出1-100内的奇数

# i = 0
# while i<101:
#     if i%2!=0:
#         print (i)
#     i+=1

#求1-2+3-4+5 ... 99的所有数的和  奇数和偶数
# i=0
# sum=0
# while i < 100:
#     if i%2==0 :
#         sum=sum+i
#         #print (sum)
#         i+=1
#     else:
#         sum=sum-i
#         i+=1
#         #print (sum)
# print (sum)
#
#
#
#
# li = [{'username':'alex','password':'SB'},
#      {'username':'wusir','password':'sb'},
#      {'username':'taibai','password':'123'},]
# a=0
# b=0
# while a < 3:
#
#     username = input("请输入你的用户名：")
#     passwd = input("请输入你的密码：")
#     for i in li:
#
#        if username == i['username'] and passwd == i['password']:
#             print('登录成功')
#             exit()
#     else:
#         print("登录失败请重新登录")
#     a += 1
#     b += 1
#     if a == 3:##当第一次的机会用完之后，在给她三次机会
#         a=0
#         if b  == 6: ##当b=6的时候就已经循环了两次，所有退出占整个循环
#             print ("你的六次机会已经全部用完，拜拜！")
#             break
#         m=input("还可以给你三次机会，请输入Y:")
#         if m=="Y":
#             continue
#         else:
#             print ("臭不要脸,你已经放弃了在玩三次的机会。")
#             break


#






















