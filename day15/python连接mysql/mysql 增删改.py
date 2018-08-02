import pymysql
# username=input('请输入用户名：')
# pwd=input('请输入密码：')

#连接数据库
conn = pymysql.connect(host='localhost',user='root',password='123',db='user')

#创建游标
cursor=conn.cursor()
#增
sql="insert into t1(id,name,pwd) values (%s,%s,%s)"
#res=cursor.execute(sql,(2,'hu','123'))
res=cursor.executemany(sql,[(3,"root","123456"),(4,"lhf","12356"),(5,"eee","156")])
print(res)

#提交
conn.commit()
#关闭游标
cursor.close()
#关闭连接
conn.close()
