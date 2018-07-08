goods = [{"name": "电脑", "price": 1999},
           {"name": "鼠标", "price": 10},
         {"name": "游艇", "price": 20},
         {"name": "美女", "price": 998},]
new_list=[]

b = 1
for v in goods:  #去循环goods列表然后给加入id
    v['id'] =  b
    b+=1
#print (goods)
salry = input ("请输入你的金额：")
while True:
    for i in goods:

        print ( str(i.get("id"))+"\t"+i.get("name") + "\t" + str(i.get("price")))

    m = input ("请输入你要购买的商品序号：").strip()
    if not m.isdigit() or m == '':
        print ("您输入的不是数字，请重新输入：")
        continue
    num = input("请输入你想要购买的个数：").strip()
    if not num.isdigit():
        print ("请输入数字:")
        continue

    for j in goods:  ##把你上面购买的商品加入到一个新的列表里
        if int(m) == j.get('id'):
            new_list.append((j.get('name'),j.get('price'),int(num)))
    for v in new_list: #去循环新的列表然后打印出数量和价格
        c=v[1] * v[2]  ##数量乘以金额

        yue=int(salry) - int(c)
        #print (yue)
        if yue < 0:
            print ("你的余额不足:")

        else:
            print ("你一共花费{}元,还剩{}元".format(c,yue))
    break











