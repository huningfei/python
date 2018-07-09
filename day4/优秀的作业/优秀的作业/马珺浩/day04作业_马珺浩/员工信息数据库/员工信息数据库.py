'''
文件存储格式如下：
id，name，age，phone，job
1,Alex,22,13651054608,IT
2,Egon,23,13304320533,Tearcher
3,nezha,25,1333235322,IT

现在需要对这个员工信息文件进行增删改查。
基础必做：
a.可以进行查询，支持三种语法：
select 列名1，列名2，… where 列名条件
支持：大于小于等于，还要支持模糊查找。
示例：
select name, age where age>22
select * where job=IT
select * where phone like 133

进阶选做：

b.可创建新员工记录，id要顺序增加c.可删除指定员工记录，直接输入员工id即可
d.修改员工信息
语法：set 列名=“新的值” where 条件
#先用where查找对应人的信息，再使用set来修改列名对应的值为“新的值”

注意：要想操作员工信息表，必须先登录，登陆认证需要用装饰器完成
其他需求尽量用函数实现
'''

__author__ = 'Junhao Ma'

from prettytable import PrettyTable

# 首先定义一个字典，记录当前用户登录状态
verify_status = {'name': None, 'status': None}
pwd_dic = {}


# 定义装饰器，操作前验证用户是否登录
# staff_pwd为密码本
def verify(func):
    def inner(*args, **kwargs):
        if verify_status['name'] and verify_status['status']:
            return func(*args, **kwargs)
        else:
            with open('staff_pwd', 'r', encoding='utf-8') as f_read:
                line = f_read.read().split('\n')
                for msg in line:
                    pwd_dic[msg.split()[0]] = msg.split()[1]
            name = input('Please input your name:').strip()
            pwd = input('Please input your password:').strip()
            if name in pwd_dic:
                if pwd == pwd_dic[name]:
                    verify_status['name'] = name
                    verify_status['status'] = True
                    return func(*args, **kwargs)
            else:
                pass

    return inner


# 登录方式1
def login1():
    cmd_inp_list = cmd_inp.split()
    if '-u' in cmd_inp_list and '-p' in cmd_inp_list and len(cmd_inp.split()) == 5:
        name_num = cmd_inp_list.index('-u') + 1
        pwd_num = cmd_inp_list.index('-p') + 1
        with open('staff_pwd', encoding='utf-8') as f_read:
            line = f_read.read().split('\n')
            for msg in line:
                pwd_dic[msg.split()[0]] = msg.split()[1]
        if cmd_inp_list[name_num] in pwd_dic:
            if cmd_inp_list[pwd_num] == pwd_dic[cmd_inp_list[name_num]]:
                verify_status['name'] = cmd_inp_list[name_num]
                verify_status['status'] = True
                print('Login successful!')
    else:
        print('Error input!')


# 语法纠正：不论输入命令行结尾有没有‘；’，都在源码中先删掉，方便取值
def grammar(sent):
    if sent.endswith(';'):
        sent = sent[:len(sent) - 1]
    else:
        sent = sent
    return sent


# select语法函数
def select(func):
    inp_list = func.split()
    # 列名查找
    if len(inp_list) == 4 and inp_list[2] == 'where':
        with open('员工信息.txt', encoding='utf-8') as f_read:
            # [id，name，age，phone，job]
            line_title = f_read.readline()[:-1].split('，')
            # 选择的元素为全局
            if '*' in inp_list[1]:
                sel_table = PrettyTable(line_title)
                f_read.seek(31)
                msg_lis = f_read.read().split('\n')
                for line in msg_lis:
                    # 遍历所有列表，并列表形式切割
                    line_lis_all = line.split(',')
                    # 筛选有用的元素，首先将判断语句摘出来
                    cond_sent = inp_list[3]
                    if '>' in cond_sent:
                        cond_lis = cond_sent.split('>')
                        cond_ele = cond_lis[0]
                        cond_val = cond_lis[1]
                        cond_ele_num = line_title.index(cond_ele)
                        if line_lis_all[cond_ele_num] > cond_val:
                            sel_table.add_row(line_lis_all)
                    if '<' in cond_sent:
                        cond_lis = cond_sent.split('<')
                        cond_ele = cond_lis[0]
                        cond_val = cond_lis[1]
                        cond_ele_num = line_title.index(cond_ele)
                        if line_lis_all[cond_ele_num] < cond_val:
                            sel_table.add_row(line_lis_all)
                    if '=' in cond_sent:
                        cond_lis = cond_sent.split('=')
                        cond_ele = cond_lis[0]
                        cond_val = cond_lis[1]
                        cond_ele_num = line_title.index(cond_ele)
                        if cond_val == line_lis_all[cond_ele_num]:
                            sel_table.add_row(line_lis_all)
                print(sel_table)
            # 选择元素为多元素
            # and后是为避免输错元素拼写而报错设置
            if ',' in inp_list[1] and set(inp_list[1].split(',')) < set(line_title):
                # 筛选select后的元素列表
                ele_lis = inp_list[1].split(',')
                sel_table = PrettyTable(ele_lis)
                # 将判断语句筛选出来
                cond_sent = inp_list[3]
                num_lis = []
                # 将select后的多元素的索引值，存入一个列表备用
                for ele in ele_lis:
                    num_lis.append(line_title.index(ele))
                f_read.seek(31)
                # 标题后的所有数据，以每行列表的形式取出
                msg_lis = f_read.read().split('\n')
                # 逐行判断，并把一行的值转换成一个列表line_lis_all
                for line in msg_lis:
                    line_lis_all = line.split(',')  # 所有类型都在
                    line_lis_need = []
                    if '>' in cond_sent:
                        cond_lis = cond_sent.split('>')
                        cond_ele = cond_lis[0]  # 类型
                        cond_val = cond_lis[1]  # 值
                        cond_ele_num = line_title.index(cond_ele)  # 根据类型找出该值在line_lis_all的索引
                        if line_lis_all[cond_ele_num] > cond_val:  # 判断，如果True：
                            for num in num_lis:  # 开始索引取值，取值取的是select的多元素类型
                                line_lis_need.append(line_lis_all[num])  # 只筛选要的值
                            sel_table.add_row(line_lis_need)  # 添加到表中
                    if '<' in cond_sent:
                        cond_lis = cond_sent.split('<')
                        cond_ele = cond_lis[0]
                        cond_val = cond_lis[1]
                        cond_ele_num = line_title.index(cond_ele)
                        if line_lis_all[cond_ele_num] < cond_val:
                            for num in num_lis:
                                line_lis_need.append(line_lis_all[num])
                            sel_table.add_row(line_lis_need)
                    if '=' in cond_sent:
                        cond_lis = cond_sent.split('=')
                        cond_ele = cond_lis[0]
                        cond_val = cond_lis[1]
                        cond_ele_num = line_title.index(cond_ele)
                        if line_lis_all[cond_ele_num] == cond_val:
                            for num in num_lis:
                                line_lis_need.append(line_lis_all[num])
                            sel_table.add_row(line_lis_need)
                print(sel_table)
            # 选择元素为单一元素
            else:
                if inp_list[1] in line_title:
                    # ele_lis用作打印表格title
                    ele_lis = []
                    ele_lis.append(inp_list[1])
                    # ele_lis_num用于索引表的元素
                    ele_lis_num = line_title.index(inp_list[1])
                    sel_table = PrettyTable(ele_lis)
                    f_read.seek(31)
                    msg_lis = f_read.read().split('\n')
                    for line in msg_lis:
                        line_lis_all = line.split(',')
                        line_lis_need = []
                        cond_sent = inp_list[3]
                        if '>' in cond_sent:
                            cond_lis = cond_sent.split('>')
                            cond_ele = cond_lis[0]
                            cond_val = cond_lis[1]
                            cond_ele_num = line_title.index(cond_ele)
                            if line_lis_all[cond_ele_num] > cond_val:
                                line_lis_need.append(line_lis_all[ele_lis_num])
                                sel_table.add_row(line_lis_need)
                        if '<' in cond_sent:
                            cond_lis = cond_sent.split('<')
                            cond_ele = cond_lis[0]
                            cond_val = cond_lis[1]
                            cond_ele_num = line_title.index(cond_ele)
                            if line_lis_all[cond_ele_num] < cond_val:
                                line_lis_need.append(line_lis_all[ele_lis_num])
                                sel_table.add_row(line_lis_need)
                        if '=' in cond_sent:
                            cond_lis = cond_sent.split('=')
                            cond_ele = cond_lis[0]
                            cond_val = cond_lis[1]
                            cond_ele_num = line_title.index(cond_ele)
                            if line_lis_all[cond_ele_num] == cond_val:
                                line_lis_need.append(line_lis_all[ele_lis_num])
                                sel_table.add_row(line_lis_need)
                    print(sel_table)
    # 模糊查找
    if len(inp_list) == 6 and inp_list[2] == 'where' and inp_list[4] == 'like':
        with open('员工信息.txt', 'r', encoding='utf-8') as f_read:
            # [id，name，age，phone，job]
            line_title = f_read.readline()[:-1].split('，')
            # 选择元素为全局
            if '*' in inp_list[1]:
                sel_table = PrettyTable(line_title)
                if inp_list[3] in line_title:
                    # 索引关键字位置
                    num_word = line_title.index(inp_list[3])
                    f_read.seek(31)
                    msg_lis = f_read.read().split('\n')  # 多行
                    for line in msg_lis:
                        word_lis = line.split(',')  # 对应值
                        if inp_list[5] in word_lis[num_word]:
                            sel_table.add_row(word_lis)
                print(sel_table)
            # 选择元素为多元素
            # and后是为避免输错元素拼写而报错设置
            if ',' in inp_list[1] and set(inp_list[1].split(',')) < set(line_title):
                # 只打印选定的元素
                ele_lis = inp_list[1].split(',')
                sel_table = PrettyTable(ele_lis)
                # 索引选定值的位置存入列表
                ele_num_lis = []
                for ele_word in ele_lis:
                    ele_num_lis.append(line_title.index(ele_word))
                if inp_list[3] in line_title:
                    # 索引关键字位置
                    num_word = line_title.index(inp_list[3])
                    f_read.seek(31)
                    msg_lis = f_read.read().split('\n')
                    for line in msg_lis:
                        word_lis = line.split(',')
                        word_print_lis = []
                        if inp_list[5] in word_lis[num_word]:
                            # 按之前找好的选定元素找对应值
                            for ele_num in ele_num_lis:
                                word_print_lis.append(word_lis[ele_num])
                            sel_table.add_row(word_print_lis)
                print(sel_table)
            # 选择元素为单一元素
            else:
                if inp_list[1] in line_title:
                    title_print = []
                    title_print.append(inp_list[1])
                    sel_table = PrettyTable(title_print)
                    # 索引选定制的位置并记录
                    ele_num = line_title.index(inp_list[1])
                    if inp_list[3] in line_title:
                        # 索引关键字位置
                        num_word = line_title.index(inp_list[3])
                        f_read.seek(31)
                        msg_lis = f_read.read().split('\n')
                        for line in msg_lis:
                            word_lis = line.split(',')
                            word_print_lis = []
                            if inp_list[5] in word_lis[num_word]:
                                word_print_lis.append(word_lis[ele_num])
                                sel_table.add_row(word_print_lis)
                    print(sel_table)


# insert语法函数，属于添加员工信息表，需验证登陆登陆状态
@verify
def insert(func):
    inp_lis = func.split()
    with open('员工信息.txt', 'r', encoding='utf-8') as f_read:
        pass


# 主程序开始
while True:
    login_flag = True
    while login_flag:
        cmd_inp = input('[root@foundation ~]# ').strip()
        if len(cmd_inp) != 0 and cmd_inp.split()[0] == 'mysql':
            # 以mysql -u [username] -p [password]的方式进入
            if len(cmd_inp.split()) > 1:
                login1()
                if verify_status['status']:
                    login_flag = False
            # 直接进入mysql，用户、登录状态空
            if len(cmd_inp.split()) == 1:
                login_flag = False
    sql_flag = True
    while sql_flag:
        sql_cmd = input('>>>>:').strip()
        sql_cmd = grammar(sql_cmd)
        # 浏览整个数据库数据
        if sql_cmd == 'show database':
            with open('员工信息.txt', encoding='utf-8') as f_read:
                table = PrettyTable(f_read.readline().split('，'))
                msg = f_read.read().split('\n')
                for line in msg:
                    table.add_row(line.split(','))
            print(table)
        if len(sql_cmd) != 0 and sql_cmd.split()[0] == 'select':
            select(sql_cmd)
        if len(sql_cmd) != 0 and sql_cmd.split()[0] == 'delete':
            pass
        if len(sql_cmd) != 0 and sql_cmd.split()[0] == 'insert':
            insert(sql_cmd)
        if len(sql_cmd) != 0 and sql_cmd.split()[0] == 'set':
            pass
        # 退出数据库时注销当前用户登录状态
        if sql_cmd == 'exit':
            sql_flag = False
            login_flag = True
            verify_status['name'] = None
            verify_status['status'] = None
