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
left_yuju="update age=35 from  userinfo  where name=wusir"
filter_cols = left_yuju.split('from')[0].split()[1].split('=')
res = [i.strip() for i in filter_cols]
print(filter_cols)
print(res)

# b = ','.join(filter_cols)
# print(b.strip())

#先循环where条件
