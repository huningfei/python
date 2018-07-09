#博客地址 http://www.cnblogs.com/huningfei/

goods = [{"name": "电脑", "price": 1999},
           {"name": "鼠标", "price": 10},
         {"name": "游艇", "price": 20},
         {"name": "美女", "price": 998},]
shopping_list = []
money = int(input("请输入你的金额：").strip())
print("商品列表")
while True:
    for i in range (len(goods)):
        print(i,goods[i]["name"],goods[i]["price"])  ##打印商品列表

    num = input("请输入你想购买的商品ID,退出请按q:").strip()
    if not num:
        print("请重新输入：")
        continue
    if num.isdigit():
        num = int(num)
        buy_num = input("请输入你想要购买的个数：").strip()
        if not buy_num:
            print ("请重新输入数字：")
            continue
        if buy_num.isdigit():
            buy_num = int(buy_num)
            if (goods[num]["price"] * buy_num) < money:  ##如果价钱小于你的金额就购买成功
                print ("你已经购买成功")
                a = 1
                while a <= buy_num:  ##循环购买的个数，然后加入到新的列表里面
                    shopping_list.append({"name": goods[num]["name"],"price": goods[num]["price"],"num":buy_num})
                    print(shopping_list)
                    a += 1
                money = money - (goods[num]["price"] * buy_num)  ##计算余额 价钱乘以个数
                print("余额: %s" %(money))
                choice = input("你还想继续购买吗，请按y，否则请按q:").strip()
                if choice == "y" or choice == "Y":
                    continue
                else:    ##如果不想购买则打印订单和消费金额
                    money = 0
                    for j in range(len(shopping_list)):  ##去循环新的列表
                        print ("订单%s: %s %s元" % (j+1,shopping_list[j]["name"],shopping_list[j]["price"]))
                        money = money + shopping_list[j]["price"]
                    print("一共消费:%s" % (money))
                    break
            else:
                print("余额不足")
    if num == "q" or num == "Q":
        print("你没有购买任何商品，谢谢光临！")
        break




