
goods = [{"name": "电脑", "price": 1999},
           {"name": "鼠标", "price": 10},
         {"name": "游艇", "price": 20},
         {"name": "美女", "price": 998},]
shopping_car = []
salry = int(input("请输入你的金额：").strip())
while True:
    print("商品列表！")
    for i in range(len(goods)):  ##给商品列表加上id,去循环goods的长度
        print(i, goods[i]["name"], goods[i]["price"])

    buy = input("请输入你要购买的商品ID  退出：Q：").strip()
    if not buy:continue   ##如果是空，请继续输入
    if buy.isdigit():
        buy = int(buy)
        buy_num = input("请输入你购买的数量：").strip()
        if not buy_num: continue ##如果是空，请继续输入
        if buy_num.isdigit():
            buy_num = int(buy_num)
            if (goods[buy]["price"] * buy_num) < salry:  ##判断商品价格是否小于你输入的金额
                print("购买成功")
                count = 1
                while count <= buy_num:  ##买几个循环几次，
                    shopping_car.append({"name": goods[buy]["name"], "price": goods[buy]["price"]})  ##把购买的商品加入到你的shoping_car列表里
                    count += 1
                salry = salry - (goods[buy]["price"] * buy_num)  ##计算余额
                print("余额：%s" % (salry))
                choice_goon = input("是否继续购买,如果想请按y,否则按q：")
                if choice_goon == "y" or choice_goon == "Y":
                    continue
                else:   ##退出的时候打印你已经购买的商品列表
                    price = 0
                    for i in range(len(shopping_car)):
                        # print(i)
                        print("订单%s： %s  %s￥" % (i, shopping_car[i]["name"], shopping_car[i]["price"]))
                        price = price + shopping_car[i]["price"] ##计算一共消费多少钱
                    print("一共消费:%s" % (price,))
                    break
            else:
                print("金额不够！")
    if buy == "q" or buy =="Q":
        print("你没购买商品")
        break

#
#
#




