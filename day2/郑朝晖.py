goods = [{"name": "电脑", "price": 1999}, {"name": "鼠标", "price": 10}, {"name": "游艇", "price": 20}, {"name": "美女", "price": 998}]
flag = True
buyProduct = dict()
buyNumCode = []
money = int(input("请输入你的存额:"))
while flag:
    print('%s %s %s' % ('商品编号', '商品名称', '商品价格'))
    for numCode in range(len(goods)):
        product = goods[numCode]
        print('%(id)5d %(name)7s %(price)8d' % {'id': numCode, 'name': product.get("name"), 'price': product.get("price")})

    numCode = int(input("请选择你要购买商品编号:"))
    count = int(input("请输入你要购买的数量:"))

    buyTotal = goods[numCode].get("price") * count
    if buyTotal > money:
        choiceYN = input("你的余额不足,是否选择购买其它商品，Y/N:")
        if choiceYN == "Y" or choiceYN == "Y".lower():
            continue
        else:
            flag = False

    else:
        money -= buyTotal
        if numCode in buyNumCode:
            count = buyProduct.get(numCode).get("count") + count
            buyProduct.get(numCode).update(count=count)
        else:
            buyNumCode.append(numCode)
            buyProduct.update({numCode: {"name": goods[numCode].get("name"), "price": goods[numCode].get("price"), "count": count}})

        choiceYN = input("你还需要购买其它商品吗，Y/N: ")
        if choiceYN == "Y" or choiceYN == "Y".lower():
            continue
        else:
            break

if len(buyProduct) == 0:
    print("你没有购买任何商品，你的金额为:{}".format(money))
else:
    consumeTotal = 0
    print("你购买的商品为：")
    print("{:^} {:^} {:^} {:^}".format("商品名称", "商品价格", "商品数量", "商品价格"))
    for k, v in buyProduct.items():
        print('{:>4s} {:>6d} {:>8d} {:>8d}'.format(v.get("name"), v.get("price"), v.get("count"), v.get("price") * v.get("count")))
        consumeTotal = consumeTotal + v.get("price") * v.get("count")

    print("你总共花费金额为:{},还剩金额为:{}".format(consumeTotal, money))