import pymysql
# username=input('请输入用户名：')
# pwd=input('请输入密码：')

#连接数据库
conn = pymysql.connect(host='localhost',user='root',password='123',db='user')

#创建游标
cursor=conn.cursor()
#增
sql="select * from t1"
rows=cursor.execute(sql)
# res1=cursor.fetchone()  #fetchone查看一行记录
# res2=cursor.fetchone()
# res3=cursor.fetchone()
# res4=cursor.fetchmany(2)#查看两行，以元祖形式出现
res5=cursor.fetchall()#查看所有记录
# print(res1)
# print(res2)
# print(res3)
# print(res4)
print(res5)

#提交
conn.commit()
#关闭游标
cursor.close()
#关闭连接
conn.close()
'''

((1, 'egon', '123'), (2, 'hu', '123'), (3, 'root', '123456'), (4, 'lhf', '12356'), (5, 'eee', '156'))
'''