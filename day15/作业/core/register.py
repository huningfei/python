from conf import setting
from core import loging
import pymysql

log=loging.mylog()
# 注册函数
def register():
    conn = pymysql.connect(host=(setting.host), user=(setting.user), password=(setting.password),
                           database=(setting.database), charset=(setting.charset))
    cursor = conn.cursor()
    count = 0
    while count < 3:
        count += 1
        user = input('用户名:').strip()
        pwd = input('密码:').strip()
        sql2 = "select * from t1 where user=%s"
        res2 = cursor.execute(sql2, [user])  # 执行sql语句，返回sql查询成功的记录数目
        if res2:
            print('用户名已存在')
            log.warning('用户名已经存在')
        else:

            # 执行完毕返回的结果集默认以元组显示
            sql = "insert into t1(user,pwd) values (%s,%s)"
            res = cursor.execute(sql, [user, pwd])  # 执行sql语句，返回sql查询成功的记录数目

            if res:
                print('注册成功')
                log.info('注册成功')
                conn.commit()
                quit()
            else:
                print('注册失败')
                log.error("注册失败")
                continue


    cursor.close()
    conn.close()
