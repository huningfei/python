#!/usr/bin/env python3
# day4博客地址：http://www.cnblogs.com/spf21/p/8919716.html

from tabulate import tabulate
import os

user_status = {"user": None, "status": False}

FILE_PATH = "./file/"

TABLE_PATH = "./table/"

TABLE = "%suser_info" % TABLE_PATH

USER_FILE = "%suser_list" % FILE_PATH

readme = "%shelp_file" % FILE_PATH


def mysql_help():
    """
    帮助文档
    :return:
    """
    with open(readme, mode="r", encoding="utf-8") as f1:
        print("*" * 100)
        for i in f1:
            print(i, end="")
        print("\n" + "*" * 100)
        

def print_log(meg, type_info="error"):
    """
    修改输出颜色
    :param meg:
    :param type_info:
    :return:
    """
    if type_info == "info":
        print("\033[32;0m%s\033[0m" % meg)
    elif type_info == "error":
        print("\033[31;0m%s\033[0m" % meg)


def table_list(path):
    """
    获取所有的表
    :param path:
    :return:
    """
    for root, dirs, files in os.walk(path):
        return files


def show_tables():
    """
    查看所有的表
    :return:
    """
    for i in T_LIST:
        print_log(i)


def wrapper(main_func):
    """
    登录装饰器
    :param main_func:
    :return:
    """
    def inner(*args, **kwargs):
        if user_status["user"] and user_status["status"]:
            result = main_func(*args, **kwargs)
            if result != None:
                return result
        else:
            str_func = "%s " % (main_func,)
            if "blog_exit" in str_func:
                print_log("Bye Bye!!!".center(40, "-"), "error")
                exit()
            if "log_out" in str_func:
                print_log("用户未登录!!!", "error")
                exit()
            print(">>>欢迎登录MySQL:")
            count = 0
            while count < 3:
                username = input("请输入用户名：").strip()
                password = input("请输入密码：").strip()
                if not username or not password:
                    print_log("用户名或密码不能为空", "error")
                with open(USER_FILE) as f1:
                    for i in f1:
                        user, passwd = i.split()
                        if username == user and password == passwd:
                            print_log("登录成功！欢迎:<%s>" % (username,))
                            user_status["user"] = username
                            user_status["status"] = True
                            main_func()
                    else:
                        print_log("用户名或者密码错误，请重试！")
                count += 1
            else:
                exit()
    return inner


def local_table(t_file):
    """
    把文件转换成字典类型  {'id': ['1', '2', '3'],
                        'name': ['Alex', 'Egon', 'nezha'],
                        'age': ['22', '23', '25'],
                        'phone': ['13651054608', '13304320533', '1333235322'],
                        'job': ['IT', 'Tearcher', 'IT']}
    :param t_file:
    :return:
    """
    n = 1
    table_dic = {}
    line_info_tmp = []
    with open(t_file) as f1:
        for line in f1:
            line = line.strip()
            # global line_title # 生命一个全局变量
            if n == 1:
                global line_title  # 生命一个全局变量
                line_title = line.split(",")
            else:
                global line_info
                line_info = line.split(",")
                line_info_tmp.append(line_info)
            n += 1
    count = 0
    for i_title in line_title:  # line_title = [id,name,age,phone,job]
        table_dic[i_title] = []
        for i_info in line_info_tmp:  # line_info_tmp = [[1,alex,22,185422342342,it], [2,spf,22,185422342342,it]]
            table_dic[i_title].append(i_info[count])
        count += 1
    # print(table_dic)
    return table_dic


def local_file(argv):
    """
    把修改后的字典写入到文件中
    :param arv: = 修改后的Table_DATA {'id': ['1', '2', '3'],
                        'name': ['Alex', 'Egon', 'nezha'],
                        'age': ['22', '23', '25'],
                        'phone': ['13651054608', '13304320533', '1333235322'],
                        'job': ['IT', 'Tearcher', 'IT']}
    :return:
    """
    #  ['1', '2', '3'] ['Alex', 'Egon', 'nezha'] ['22', '23', '25'] # [1,alex,22] # 1,alex,22
    #  把字典转换成列表，在转成字符串写入到新的表文件，删除旧表文件，重命名新文件为旧文件
    with open("info.bak", mode="a", encoding="utf-8") as f1:
        title = ",".join(line_title)   # 获取title转换成字符串写入文件
        f1.write(title + "\n")
        # li = []  #  [['1', 'Alex', '22', '13651054608', 'linux'], ['2', 'Egon', '23', '13304320533', 'Tearcher'], ['3', 'nezha', '25', '1333235322', 'linux']]
        # for i in range(len(argv["id"])):
        #     li_tmp = []  # li1 = ['1', 'Alex', '22', '13651054608', 'IT']
        #     for f in line_title:
        #         li_tmp.append(argv[f][i])
        #     li.append(li_tmp)
        li = zip(*argv.values())
        for i in li:
            info = ",".join(i)
            f1.write(info + "\n")
    os.remove(TABLE)
    os.rename("info.bak", TABLE)

    
def syntax_select(where_data, query_section):
    """
    把where返回的结果根据字段打印出来
    :param where_data:  [['2', 'Egon', '23', '13304320533', 'Tearcher'], ['3', 'nezha', '25', '1333235322', 'IT']]
    :param query_section: # select name,age from info  select * from info
    :return:
    """
    fields_tmp = query_section.split("from")[0].split("select")[1].split(",")  # 切割 query_section 成列表["age","name"]
    fields = [i.strip() for i in fields_tmp]  # 去掉关键字的空格
    for t_name in T_LIST:
        if t_name in query_section:
            if "*" in fields:
                fields = line_title
            res_li = []  # 用于存储匹配到的字段内容 每条记录以列表方式存储  res_li = [[23 ,Egon] ,[34,alex]]
            try:
                for i in where_data:   # 循环 where查的数据  ['2', 'Egon', '23', '13304320533', 'Tearcher']   ['3', 'nezha', '25', '1333235322', 'IT']]
                    li = []  # 存储字段对应的单条数据   li = [23,] --> li = [23 ,Egon]  age：li = [alex,22]  name = [Egon,34]
                    for k in fields:  # k = "age" k = "name"  fields = [age,name]
                        try:                                                                 # i = ['2', 'Egon', '23', '13304320533', 'Tearcher']
                            index = line_title.index(k)  # 返回字段对应的索引  #  line_title = [id ,name, age ,phone,job]  # age = 2  # name = 1
                            li.append(i[index])  # 添加字段对应的数据到列表 i = ['2', 'Egon', '23', '13304320533', 'Tearcher']
                        except ValueError:
                            print_log("语法错误：%s列不存在！" % k)
                            return
                    res_li.append(li)
                print(tabulate(res_li, headers=fields, tablefmt="grid"))
                print_log("查到了%s行！" % len(where_data), "info")
                return
            except TypeError:
                print_log("语法错误：where没有跟条件", where_data)
                return
    else:
        print_log("语法错误：表不存在")
        return


def syntax_insert(where_data, query_section):
    """
    插入
    :param where_data:
    :param query_section: insert into info values(3,nezha,25,1333235322,IT);
    :return:
    """
    if "values" in query_section:
        res_tmp = query_section.split("values")[1].split(",")
        res = [i.strip("()").strip() for i in res_tmp]
        if res[0].isdigit():
            res[0] = str(int(Table_DATA["id"][-1]) + 1)
        res_w = ",".join(res)
        if len(res) != len(line_title):
            print_log("语法错误：需要%s个参数，你给了%s个" % (len(line_title), len(res)), "error")
            return
        else:
            if res[0] in Table_DATA["id"]:
                print_log("语法错误：ID重复", "error")
            else:
                if res[3] in Table_DATA["phone"]:
                    print_log("语法错误：手机号重复")
                else:
                    with open(TABLE, mode="a") as f1:
                        f1.write(res_w + "\n")
    else:
        print_log("语法错误：缺少values")
        return


def syntax_update(where_data, query_section):
    """
    更新
    :param where_data: = [['2', 'Egon', '23', '13304320533', 'Tearcher'], ['3', 'Egon', '23', '13304320533', 'Tearcher']]
    :param query_section:  = update info set age = 25
    :return:
    """
    #  根据 where_data 的id获取Table_DATA["id"]的索引，在根据索引去Table_DATA[字段]修改值
    if "set" in query_section and "=" in query_section:  # 判断语法是否有set
        res_tmp = query_section.split("set")[1].split("=")  # 取出需要修改的字段和值
        res = [i.strip() for i in res_tmp]  # 去掉空格res =  ["age", "25"]
        if where_data == None:
            print_log("语法错误：where语法有错，示例：where  age > 23")
            return
        for line in where_data:  # ['2', 'Egon', '23', '13304320533', 'Tearcher']
            line_id = line[0]  # 获取匹配到内容的ID  # line_id = 2
            index = Table_DATA["id"].index(line_id)  # index = id  在 Table_DATA表id列的索引   index = 1
            Table_DATA[res[0]][index] = res[1]  # Table_DATA[res["age"]]  =  [22,23,30]
        print_log("影响了%s行！" % len(where_data), "info")
        return Table_DATA
    else:
        print_log("语法错误：缺少set或者 = ", "error")
        return
    # print(where_data)


def syntax_delete(where_data, query_section):
    """
    根据where条件删除匹配行
    :param where_data:  = [['1', 'Alex', '22', '13651054608', 'IT'], ['3', 'nezha', '25', '1333235322', 'IT']]
    :param query_section: delete from info
    :return:
    """
    if "from" in query_section:  # 判断语法是否有from
        if where_data == None:
            print_log("语法错误：where语法错误，示例：where age > 23")
            return
        for line in where_data:
            line_id = line[0]  # 获取匹配到内容的ID
            index = Table_DATA["id"].index(line_id)  # index = id  在 Table_DATA表id列的索引
            for dic_line in Table_DATA:  # 删除获取到的索引对应多有值
                Table_DATA[dic_line].pop(index)
        print_log("影响了%s行！" % len(where_data), "info")
        return Table_DATA
    else:
        print_log("语法错误：from", "error")
        return


def op_gt(argv_fields, argv_value):
    """
    大于判断：
        根据判断返回数据，以列表的方式
    :param argv_fields: 字段：age
    :param argv_value:  判断的值：22
    :return:
    """
    data_res = []  # 空列表接受所有匹配到的参数
    for index, value in enumerate(Table_DATA[argv_fields]):  # 循环列表进行匹配，index记录匹配元素的索引
        try:
            if float(value) > float(argv_value):  # 匹配参数
                l1 = []  # 空列表接受匹配到的单行
                for key in Table_DATA.keys():  # 循环用户表获取匹配到的完整行
                    l1.append(Table_DATA[key][index])  # 根据索引匹配 并把匹配到的行添加到小列表中
                data_res.append(l1)  # 匹配到的行将以列表数据类型的存在data_res中
        except ValueError:
            print_log("语法错误：字符串类型错误")
            return
    return data_res


def op_lt(argv_fields, argv_value):
    """
    小于判断：
        根据判断返回数据，以列表的方式
    :param argv_fields: 字段：age
    :param argv_value:  判断的值：22
    :return:
    """
    data_res = []
    for index, value in enumerate(Table_DATA[argv_fields]):
        if float(value) < float(argv_value):
            l1 = []
            for key in Table_DATA.keys():
                l1.append(Table_DATA[key][index])
            data_res.append(l1)
    return data_res


def op_eq(argv_fields, argv_value):
    """
    等于判断：
        根据判断返回数据，以列表的方式
    :param argv_fields: 字段：age
    :param argv_value:  判断的值：22
    :return:
    """
    data_res = []
    for index, value in enumerate(Table_DATA[argv_fields]):
        if value == argv_value:
            l1 = []
            for key in Table_DATA.keys():
                l1.append(Table_DATA[key][index])
            data_res.append(l1)
    return data_res


def op_like(argv_fields, argv_value):
    """
    模糊匹配：
        根据判断返回数据，以列表的方式
    :param argv_fields: 字段：age
    :param argv_value:  判断的值：22
    :return:
    """
    data_res = []
    for index, value in enumerate(Table_DATA[argv_fields]):
        if argv_value in value:
            l1 = []
            for key in Table_DATA.keys():
                l1.append(Table_DATA[key][index])
            data_res.append(l1)
    return data_res


def where_parser(section):
    """
    where条件解析
    :param section: 条件: age > 22
    :return:
    """
    choice = {
        ">": op_gt,
        "<": op_lt,
        "=": op_eq,
        "like": op_like
    }
    for choice_key, func in choice.items():  # 第一次进来 choice_key = ">" func = op_gt
        if choice_key in section:  # 第一次进来 ">"   in   age > 22
            fields, value = section.split(choice_key)  # fields =  age  value = 22
            if fields.strip() in line_title:  #  fields.strip() 去掉空格   line_title = [id,name,age,job]
                where_data = func(fields.strip(), value.strip())  # 执行对应的where判断，返回判断结果
                return where_data   # 返回给语法解析器
            else:
                print_log("语法错误：%s字段不存在" % fields)
                return
    else:
        print_log("语法错误：缺少条件%s" % choice.keys(), "error")
        return


def syntax_parser(cmd):
    """
    语法分析器
    :param cmd:  语法：select name,age from info where age > 22
    :return:
    """
    choice_action = {
        "select": syntax_select,
        "insert": syntax_insert,
        "update": syntax_update,
        "delete": syntax_delete,
        "show": show_tables
    }
    cmd = cmd.strip()
    actions = ["select", "insert", "update", "delete", "show"]
    if cmd.split()[0] in actions:  # 判断用户输入的语法是否正确（["select", "insert", "update", "delete"]）
        if "where" in cmd:
            query_section, where_section = cmd.split("where")  # 根据where关键件把用户输入的命令切割成两部分，前半部分是增删改查方法，后半部分是where条件
            where_data = where_parser(where_section)  # 把where条件交给where函数进行解析判断，并返回解析判断值
            func_res = choice_action[query_section.split()[0]](where_data, query_section)  # 讲where_data返回的结果交给执行增删改成函数
            if func_res != None:
                local_file(func_res)   # func_res 等于修改后的TABLE_DATA
        else:
            query_section = cmd  # query_section 默认值等于cmd
            where_section = "id > 0"  # 条件默认为id > 0
            where_data = where_parser(where_section)  # 把where条件交给where函数进行分配判断
            action = query_section.split()[0]  # action = select ...
            if action == "show":
                show_tables()
                return
            if action == "update" or action == "delete":
                print_log("语法错误：修改或删除缺少where条件")
                return
            func_res = choice_action[action](where_data, query_section)  # 执行增删改成函数
            if func_res != None:
                local_file(func_res)   # func_res 等于修改后的TABLE_DATA
    else:
        print_log("语法错误: %s" % actions, "error")
        return


T_LIST = table_list(TABLE_PATH)

Table_DATA = local_table(TABLE)


@wrapper
def main():
    """
    主运行程序
    :return:
    """
    mysql_help()  # 显示帮助
    while True:
        global Table_DATA
        Table_DATA = local_table(TABLE)
        cmd = input("[info]>")
        if not cmd:continue
        syntax_parser(cmd)  # 把sql语句交给语法分析器（syntax_parser）处理


if __name__ == "__main__":
    main()

