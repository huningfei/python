

# cmd = "update name='bob' from  userinfo  where age=25"
# a=cmd.split('from')[0].split()[1].split('=')[1].strip("'")
# print(a)
# insert = "insert into userinfo ('name','age') values ('jack','23')"
# b = insert.split('values')[1].split()[0]
# print(b)


# b = [i.strip().strip(",") for i in a]
# print(b)
# b= ['3', 'nezha', '25', '1333235322', 'IT'][1]
# print(b)

'''
##查询语句
select id ,name, age from userinfo where age>22
select * from userinfo where age>22
select * from userinfo where age=25
select * from userinfo where phone like 133

##下面这个不行
select * from userinfo where job=IT
'''

##更改语句
# update name='bob' from  userinfo  where age=25
# cmd = 'select *  from userinfo'
# a = cmd.split('from')[0].split()[1:]
# if a==['*']:
#     print('ok')
# else:
#     print('bad')

##删除语句
# left_yuju="delete name='bob' from userinfo where age=25"
#
# filter_cols = left_yuju.split('from')[0].split()[1].split('=')
# print(filter_cols)
dic = {'id':['1','2','3','4','5']}
b = int(dic.get('id')[-1])+1
# print(b)
a = [' 5', 'hnf', '23', '123456789', 'python']
print(type(a[0]))
a[0]=b
print(a)
# with open('userinfo',encoding='utf-8',mode='a')as f1:
#     for i in a:
#         f1.write(i)