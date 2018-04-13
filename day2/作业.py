'''
购物车需求：
1 输入正确的用户名和密码，登录成功之后，输入金额，并打印购物车列表
2 用户输入序列号，购买商品，也可以指定购买数量
3 如果你输入的金额大于你要购买的商品，则把商品添加到购物车里，然后扣钱，打印剩余金额
4 如果你输入的金额小于你要购买的商品价格，则提示你余额不足，让你重新输入金额
5 如果不想买了，则输入q退出整个程序
'''

'''
goods = [{"name": "电脑", "price": 1999},
           {"name": "鼠标", "price": 10},
         {"name": "游艇", "price": 20},
         {"name": "美女", "price": 998},]
m = input("请输入你的金额：")
count = 0
print("id   商品    金额" )


new_list = []
#print (len(goods))
while True:
    for i in goods:
        count += 1
        if count > 4:
            count = 1
        print(str(count) + "\t" + i.get("name") + "\t" + str(i.get("price")))

    shopping_id = input("请输入你想购买的商品id:").strip()
    if not shopping_id.isdigit() or len(goods) < int(shopping_id):
        print ("你输入的不符合规范，请重新输入数字：")
        continue
    num = input("请输入你想购买的个数")
    if not num.isdigit():
        print ("只能输入数字")
    buytotal = int(m) * int(i.get('price'))
    print (buytotal)
    # for j in goods:
    #     if int(shopping_id) * int(j.get('price')) < int(m):
        # j.get('name')
        # j.get('price')
        #     new_list.append(j.get('name')+ j.get("price")+ int(num))
#print (new_list)

# 打印商品列表，提示输入 工资
#选择序号，如果选择的是非数字或者大于商品id，则继续输入
#选择购买数量，如果选择的是非数字也提醒继续输入
#如果选择的商品乘以价格和数量大于你的金额，则提醒金额不足，请选择其他商品
#如果购买成功，则吧新买的商品加入到你的列表里面，最后计算价格，退出
'''
goods = [{"name": "电脑", "price": 1999},
           {"name": "鼠标", "price": 10},
         {"name": "游艇", "price": 20},
         {"name": "美女", "price": 998},]
money = int(input("请输入你的金额："))
new_list=[]
while True:
    for j in goods:
        print ("%d %s %d" % (goods.index(j),j["name"],j["price"]))
    num = input("请选择你想购买的商品：")
    if not num.isdigit() or len(goods) < int(num):
        print ("你输入的不是数字，请重新输入")
        continue
    if num.isdigit():
        num = int(num)

    jishu = input("请输入你想要购买的数量：")
    if not jishu:continue
    if jishu.isdigit():
        jishu = int(jishu)
        if (goods[num]["price"] * jishu) < money:
            print ("购买成功")
            count = 1
            while count <= jishu:
                new_list.append({"name":goods[num]["name"],"price":goods[num]["price"]})

                count += 1
                print(new_list)

        # count = 1
        # while count <= jishu:
        #     new_list.append(goods[jishu]["name"])
        #     count += 1
        # print (new_list)



    # if int(num) * int(jishu) > int(money):
    #     print ("你的余额不足，请购买其他商品")


    choiceYN = input("如果你还想继续购买请输入y,不想输入n:")
    if choiceYN == 'Y' or choiceYN == "Y".lower():
            continue
    break







