import pymysql
user=input('用户名:').strip()
pwd=input('密码:').strip()
#连接数据库
conn=pymysql.connect(host='localhost',user='root',password='123',database='user',charset='utf8')
#游标
cursor=conn.cursor() #执行完毕返回的结果集默认以元组显示


#执行sql语句
sql="select * from t1 where name=%s and pwd=%s"
print(sql)
res=cursor.execute(sql,[user,pwd]) #执行sql语句，返回sql查询成功的记录数目
#print(res)

cursor.close()
conn.close()

if res:
    print('登录成功')
else:
    print('登录失败')