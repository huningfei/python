import pymysql
# username=input('请输入用户名：')
# pwd=input('请输入密码：')

#连接数据库
conn = pymysql.connect(host='localhost',user='root',password='123',db='user')

#创建游标
cursor=conn.cursor()
#增
sql="insert into t1(name,pwd) values (%s,%s)"
res=cursor.execute(sql,('hu','123'))
print(res)

#提交
conn.commit()
#关闭游标
cursor.close()
#关闭连接
conn.close()
