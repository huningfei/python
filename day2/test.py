
goods = [{"name": "电脑", "price": 1999},
           {"name": "鼠标", "price": 10},
         {"name": "游艇", "price": 20},
         {"name": "美女", "price": 998},]
new = dict()
jiage_list = []
b = 0
for v in goods:  #去循环goods列表然后给加入id
    v['id'] =  b
    b += 1
#print (goods)
salry = input ("请输入你的金额：")
while True:
    for i in goods:

        print ( str(i.get("id"))+"\t"+i.get("name") + "\t" + str(i.get("price")))
        #print ("%d%s%d % (goods.index(i),i["name"],i["price"]))

    m = input ("请输入你要购买的商品序号：").strip()
    if not m.isdigit() or m == '':
        print ("您输入的不是数字，请重新输入：")
        continue
    num = input("请输入你想要购买的个数：").strip()
    if not num.isdigit():
        print ("请输入数字:")
        continue

    new.update({m: {"name": goods[int(m)].get("name"), "price": goods[int(m)].get("price"), "num": int(num)}})
    print(new)
    buyTotal = goods[int(m)].get("price") * int(num)
    print(buyTotal)




    if int(buyTotal) > int(salry):
        print("你的余额不够，请充值")
        continue


    choiceYN = input("你还需要购买其它商品吗，Y/N: ")
    if choiceYN == "Y" or choiceYN == "Y".lower():
        continue
    else:
        break
total = 0
print("你购买的商品为：")
for k,v in new.items():
    print(v.get("name"),v.get("price") * v.get("num"))



