import pymysql
conn=pymysql.connect(host='localhost',user='root',password='123',database='user')
cursor=conn.cursor()

sql="insert into t1(name,pwd) values('aaa','123')"
rows=cursor.execute(sql)
print(cursor.lastrowid) #在插入语句后查看

conn.commit()

cursor.close()
conn.close()