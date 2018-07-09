##商品列表是个列表类型的

shangpin = [["iphone",6500],
            ["mac",10000],
            ["watch",200]
]
shopping_list = []
salry = int(input("请时输入你的工资："))
print("商品列表;")
while True:
    for i in enumerate(shangpin):
        print(i)

    buy_id = input("请时输入你的id:")
    if not buy_id:
        continue
    if buy_id.isdigit():
        buy_id=int(buy_id)
        buy_num = input("请输入你的购买个数：")
        if not buy_num:continue
        if buy_num.isdigit():
            buy_num = int(buy_num)
            if shangpin[buy_id][1] * buy_num < salry:
                print("你已经购买成功")
                a = 1
                while a <= buy_num:

                    shopping_list.append({"name": shangpin[buy_id][0],"price":shangpin[buy_id][1],"num":buy_num})
                    a += 1
                    #print(shopping_list)
                    salry = salry - (shangpin[buy_id][1] * buy_num)
                    print("你的余额是%s元" % (salry))
                    chinose = input("如果继续购买请按y,否则按q:")
                if chinose == "y" or chinose == "Y":
                    continue
                else:
                    salry = 0
                    for j in range(len(shopping_list)):
                        print("订单%s: %s %s元" % (j + 1, shopping_list[j]["name"], shopping_list[j]["price"]))
                        salry = salry + shopping_list[j]["price"]
                    print("一共消费%s元" % (salry))
                    break
            else:
                print("你的余额已经不够了，请选择购买其他商品")




