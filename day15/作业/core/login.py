from conf import setting
import pymysql

# 登录函数
def login():
    conn = pymysql.connect(host=(setting.host), user=(setting.user), password=(setting.password),
                           database=(setting.database), charset=(setting.charset))
    cursor = conn.cursor()
    count = 0
    while count < 3:
        count += 1
        user = input('用户名:').strip()
        pwd = input('密码:').strip()

        sql = "select * from t1 where user=%s and pwd=%s"
        res = cursor.execute(sql, [user, pwd])  # 执行sql语句，返回sql查询成功的记录数目
        if res:
            print('登录成功')
            quit()
        else:
            print('登录失败')
            continue

    cursor.close()
    conn.close()
