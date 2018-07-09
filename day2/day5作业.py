tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])

#c.	请问tu变量中的"k2"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 “Seven”

'''

dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
#请循环输出所# 有的key
# for i in dic.keys():
#     print(i)

#请循环输出所有的value
# for i in dic.values():
#     print(i)

#请循环输出所有的key和value
# for i in dic.items():
#     print(i)

#请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# dic["k4"] = "v4"
# print(dic)
#请在修改字典中 “k1” 对应的值为 “alex”，输出修改后的字典
# dic["k1"] = "alex"
# print(dic)

#请在k3对应的值中追加一个元素 44，输出修改后的字典
print(dic.get('k3'))
dic.get('k3').append(44)
print(dic)

#请在k3对应的值的第 1 个位置插入个元素 18，输出修改后
a = dic.get('k3')
a.insert(0,'18')
print(dic)
'''

'''
#3 题
av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌丝请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}
# 1，给此 ["很多免费的,世界最大的","质量一般"]列表第二个位置插入一个元素：'量很大'。
a = av_catalog.get("欧美").get("www.youporn.com")
a.insert(1,'量很大')
print(a)

# 2，将此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表的 "全部收费,屌丝请绕过" 删除。

b = av_catalog.get("欧美").get('x-art.com')
b.pop(1)
print(b)

# 4，将此["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]列表的 "verygood"全部变成大写。
c = av_catalog.get('日韩').get('tokyo-hot')
c2 = c[1].upper()
print(c2)

#给 '大陆' 对应的字典添加一个键值对 '1048' :['一天就封了']
d = av_catalog.get('大陆')
d1 = d["1048"] = "[一天就疯了]"
print(d)

#6，删除此"letmedothistoyou.com": ["多是自拍,高质量图片很多", "资源不多,更新慢"] 键值对。
f = av_catalog.get("欧美")
f.pop("letmedothistoyou.com")
print(f)

#给此["全部免费,真好,好人一生平安","服务器在国外,慢"]列表的第一个元素，加上一句话：'可以爬下来'
dd = av_catalog.get("大陆").get("1024")
dd.insert(0,"可以爬下来")
print(dd)
'''
#有字符串"k:1|k1:2|k2:3|k3:4" 处理成字典 {'k':1,'k1':2....}
str = "k:1|k1:2|k2:3|k3:4"
a = str.split("|")
print(a)
dic = {}
for i in a:
    b = i.split(":")  ##把大列表变成小列表
    print(b)
    dic[b[0]]=b[1]  ##赋值k
print(dic)




# 有如下值li= [11,22,33,44,55,66,77,88,99,90]，
# 将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
li= [11,22,33,44,55,66,77,88,99,90]
dic = {"k1":[],"k2":[]}
for i in li:
    if i > 66:
        dic.get("k1").append(i)

    else:
        dic.get("k2").append(i)
print(dic)





