博客地址:http://www.cnblogs.com/yimiaoyikan/
作业整体思路:
    1)用正则表达式,实现对select 的拆分,拆分出表名字\查询的列\查询条件
    2)先读取文件内容,返回一个列表,元素为字典
    3)对where条件中的逻辑进行判断,符合条件的返回true,不符合条件返回false
    4)对查询的列进行判断,如果查询的列在字典的键中,则打印对应的键值;如果是*,则打印所有的列
作业运行方式:
    右键,run.输入select 语句
实现的功能:支持一下几种语法:
    1)select * from staff
    2)select id,name from staff where id=3
    3)select id,name from staff where id>1
    4)select id,name from staff where name like lex
    5)select * from staff where 1=1


