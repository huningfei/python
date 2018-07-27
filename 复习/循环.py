# 如果while循环被break打断，就不走else

# count = 1
# while count < 5:
#     if count ==4:
#         break
#     print(count)
#     count += 1
# else:
#     print('循环正常完毕')

#打印1-10 ，7除外
# count=0
# while count <10:
#     count += 1
#     if count==7:
#         pass
#     else:
#         print(count)
#求1到100所有数之和
# a=0
# sum=0
# while a <100:
#     a=a+1
#     sum=sum+a
# print(sum)
#求1到100所有奇数之和
# a=0
# while a < 100:
#     a = a + 1
#     if a % 2 == 1:
#         print(a)
#所有偶数
# a=0
# while a < 100:
#     a = a + 1
#     if a % 2 == 0:
#         print(a)

# 求1-2+3-4+5 ... 99的所有数的和  奇数和偶数
# sum1=0#奇数
# sum2=0#偶数
# i=0
# while i <100:
#     i=i+1
#     if i%2==1:
#         sum1=sum1+i#i=3 sum1+3=0+3 i=5 就是0+5
#     else:
#         sum2=sum2+i
# print(sum1-sum2)

#用户登录三次机会
'''
user='hu'
passwd='123'
i=0
print('请注意，一共有三次登录机会')
while i <3:

    i+=1
    username=input('请输入你的用户名：')
    if username==user:
        password=input('请输入密码：')
        if password==passwd:
            print("恭喜你，登录成功")
            break
        else:
            print('你输入的密码有误,你已经用了%s次了'%(i))
    else:
        print('用户名错误,你已经用了%s次了'%(i))

'''
# msg = '老男孩python是全国范围内最好的python培训机构'
# for item in msg:
#     print(item)

li = ['alex','银角','女神','egon','太白']
for i in enumerate(li):
    print(i)

for index,name in enumerate(li):
    print(index,name)

# for index, name in enumerate(li, 100):  # 起始位置默认是0，可更改
#     print(index, name)