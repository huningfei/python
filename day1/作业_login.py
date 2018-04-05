
##1 取出列表里面的字典，然后取字典的值，即用户名和密码
#2 创建一个循环去读用户名和密码，然后和你输入的用户名和密码做比较
#3 如果成功就提示成功并跳出循环
#4 如果不成功会提示重新输入，直到第三次，会提示你在给你三次机会，如果输入要y就重新给你三次机会，否则就退出整个循环

#
li = [{'username':'alex','password':'SB'},
     {'username':'wusir','password':'sb'},
     {'username':'taibai','password':'123'},]
a=0
b=0
while a < 3:

    username = input("请输入你的用户名：")
    passwd = input("请输入你的密码：")
    for i in li:

       if username == i['username'] and passwd == i['password']:
            print('登录成功')
            exit()
    else:
        print("登录失败请重新登录")
    a += 1
    b += 1
    if a == 3:##当第一次的机会用完之后，在给她三次机会
        a=0
        if b  == 6: ##当b=6的时候就已经循环了两次，所有退出占整个循环
            print ("你的六次机会已经全部用完，拜拜！")
            break
        m=input("还可以给你三次机会，请输入Y:")
        if m=="Y":
            continue
        else:
            print ("臭不要脸,你已经放弃了在玩三次的机会。")
            break













# 博客地址   http://www.cnblogs.com/huningfei/articles/8692321.html






