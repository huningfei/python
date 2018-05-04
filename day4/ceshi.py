##查询语句
# select id ,name, age from userinfo where age>22
# select * from userinfo where age>22
# select * from userinfo where age=25
# select * from userinfo where phone like 133
# ##下面这个不行
# select * from userinfo where job=IT



##更改语句
# update name='bob' from  userinfo  where age=25
# cmd = 'select *  from userinfo'
# a = cmd.split('from')[0].split()[1:]
# if a==['*']:
#     print('ok')
# else:
#     print('bad')
# left_yuju="update age=35 from  userinfo  where name=wusir"
# filter_cols = left_yuju.split('from')[0].split()[1].split('=')
# res = [i.strip() for i in filter_cols]
# print(filter_cols)
# print(res)

# b = ','.join(filter_cols)
# print(b.strip())

#删除
#delete name=wusir from userinfo where age=35

# with open("userinfo","r",encoding="utf-8") as f:
#     lines = f.readlines()
#
# with open("userinfo","w",encoding="utf-8") as f2:
#     for line in lines:
#         if "wusir" in line:
#             continue
#         f2.write

# b={'id': ['1', '2', '3'], 'name': ['Alex', 'Egon', 'wusir'], 'age': ['23', '24', '35'],
#    'phone': ['13651054608', '13304320533', '1333235322'], 'job': ['IT\n', 'Tearcher\n', 'IT\n']}
#
# c=b.get('id')
# #print(c)
# d=b["id"].index('3') ##查出id索引
# c=b.get('name')[d]
# print(c)
#print(d)
# f = b["name"][d]#根据id索引查出name对应的值
# print(b.get('id').pop(d))
# a=b.get('name').pop(d)
# print(b.get("age").pop(d))
# print(b.get("phone").pop(d))
# print(b.get('job').pop(d))
#
# print(a)
# print(b)
# print(f)
# print(b['age'][d])

##更新语句
#left_yuju='insert into userinfo id,name,age,phone,job values 8,jack,23,123456789,python'
#
# filter_index = left_yuju.split('userinfo')[-1].split('values')[:-1]
#filter_values=left_yuju.split('values')[-1].split(',')
#
# print(filter_index,type(filter_index))
#print(filter_values)
from tabulate import tabulate
new_list=[]
with open('userinfo',encoding='utf-8',mode='r') as f1:
    new_list.append(f1.readline())

print(new_list)
# print(tabulate(new_list,tablefmt="grid"))
# insert into userinfo id,name,age,phone,job values 5,jinxing,43,123456789,python