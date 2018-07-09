import re, time, json, functools
import pandas as pd
from prettytable import PrettyTable

"""
思路：
    1.创建SqlSyntax类，初始化数据和字符串，用于处理select、insert、delete、set函数，用于处理字符串获取参数并返回
    2.创建SqlHandle类，用于反射上述函数，接收其字符串参数和数据，并执行响应的增删改查函数，添加一些边角料
    3.创建TableHandler类，用于执行循环，获取窗口输入的字符串，并调用sql_handler，返回结果
    4.创建用户认证类
"""

class SqlSyntax(object):
    """负责增删改查的SQL语句模块"""
    def __init__(self, ):
        self.string = ""
        self.dataSet = ""

    def select(self):
        """负责查找语句, 只识别 select **** where ****语句"""
        if "where" in self.string:
            par = re.compile(r"select(.+)where", flags=re.S)   # 用匹出select和where里的关键字，注意有*
            str1 = re.match(par, self.string).group(1)
            condition = self.string.split("where")[-1].strip()
        else:
            str1 = self.string.split(" ", 1)[-1]
            condition = False
        if "*" in str1:
            keys = "*"
        else:
            keys = [r.strip() for r in str1.split(",")]
        return {
            "keys": keys,
            "condition": condition,
        }

    def insert(self):
        """
        负责插入语句, 只识别 insert (name="alex", age="10000") 和 insert("alex", "10000")，必须输入所有的信息"""
        par = re.compile(".*\((.+)\).*", re.S)        # 匹配出insert 后面的内容
        str1 = re.match(par, self.string).group(1)
        if "=" not in str1:            # 说明都是元组,'"Alex", "10000"'
            keys = list(self.dataSet.columns)
            values = [self.strip(r) for r in str1.split(",")]  # 必须除去'"alex"'或者"'alex'"外边的引号
            dic = dict(zip(keys, values))
        else:
            # 说明是'name="Alex", age="10000"'这种类型,要去掉双引号
            dic = {r.split("=")[0].strip(): self.strip(r.split("=")[1]) for r in str1.split(",")}
        return dic

    def set(self):
        """负责修改语句, 只识别 set name="alex" where 条件"""
        par = re.compile(r"set(.+)where", flags=re.S)
        str1 = re.findall(par, self.string)[0]
        condition = self.string.split("where")[-1].strip()
        keys = {r.split("=")[0].strip(): self.strip(r.split("=")[1]) for r in str1.split(",")}
        return {
            "keys": keys,
            "condition": condition,
        }

    def delete(self):
        """负责删除语句, 只识别 delet * where id = 3"""
        condition = self.string.split("where")[-1].strip()
        return {
            "condition": condition,
        }

    def strip(self, string):
        return string.strip().strip("'").strip('"')

class SqlHandler(SqlSyntax):
    def __init__(self):
        super(SqlHandler, self).__init__()
        self.__func_dict = dict(
            select=self.__select_handler,
            insert=self.__insert_handler,
            set=self.__set_handler,
            delete=self.__delete_handler,
        )
    def sql_handler(self):
        try:
            func = self.string.split(" ", 1)[0]  # 找到字符串的第一个字符
            dic = getattr(self, func)()
            data = self.__func_dict[func](dic)   # 执行相应的函数
            print(self.__table(data))
            self.dataSet.to_csv('table.txt', index=None)
        except Exception as e:
            self.__log("Error.The syntax is not correct.", e)

    def __select_handler(self, dic):
        """根据dic参数执行查询结果"""
        if dic["condition"]:
            if dic["keys"] == "*":
                data = self.__where(dic["condition"])
            else:
                data = self.__where(dic["condition"])[dic["keys"]]
        else:
            if dic["keys"] == "*":
                data = self.dataSet
            else:
                data = self.dataSet[dic["keys"]]
        return data

    def __insert_handler(self, dic):
        """根据dic参数执行插入结果"""
        if dic["id"] in list(self.dataSet["id"]):
            self.__log("The id is already exist. Please input again.")
        if dic["name"] in list(self.dataSet["name"]):
            string = str(input("Warning: the name is already exist, surely insert it?"))
            if string in ["Y", "y", "yes", "YES", ""]:
                self.dataSet.loc[self.dataSet.shape[0]] = [dic.get(key) for key in list(self.dataSet.columns)]
        else:
            self.dataSet.loc[self.dataSet.shape[0]] = [dic.get(key) for key in list(self.dataSet.columns)]
        return self.dataSet

    def __set_handler(self, dic):
        """根据dic参数执行修改结果"""
        return self.__inset_and_delete(dic, "set")

    def __delete_handler(self, dic):
        # index = self.dataSet[self.dataSet["id"].isin(index)].index.tolist()  # 删除
        return self.__inset_and_delete(dic, "delete")

    def __where(self, condition):
        """处理语句"""
        key = re.match('^[0-9a-zA-Z]+', condition).group(0)
        if "like" in condition:
            value = re.findall('[0-9a-zA-Z]+$', condition)[0]   # 找到这个参数
            str_v = [str(v) for v in list(self.dataSet[key])]
            a = [value in v for v in str_v]
            data = self.dataSet.loc[a, :]
        else:
            if "=" in condition:
                index = condition.index("=")
                condition = condition[: index] + "=" + condition[index: ]
            expression = 'self.dataSet["%s"]' % key
            string = condition.replace(key, expression)
            data = self.dataSet[eval(string)]
        return data

    def __inset_and_delete(self, dic, func_name):
        msg = self.dataSet.to_dict("records")
        value = re.findall('[0-9a-zA-Z]+$', dic["condition"])[0]
        key = re.findall('^[0-9a-zA-Z]+', dic["condition"])[0]
        if func_name == "set":
            for row in msg:
                for k, v in dic["keys"].items():
                    if str(row.get(key)) == value:
                        row[k] = v
            self.dataSet = pd.DataFrame(msg, columns=self.dataSet.columns)
        else:
            msg_new = []
            for row in msg:
                if str(row.get(key)) == value:
                    pass
                else:
                    msg_new.append(row)
            self.dataSet = pd.DataFrame(msg_new, columns=self.dataSet.columns)
        self.dataSet.to_csv(self.table, index=None)
        return self.dataSet

    def __table(self, data):
        table = PrettyTable(list(data.columns))
        for i in range(data.shape[0]):
            table.add_row(data.iloc[i, :])
        return table

    def __log(self, *args, **kwargs):
        print("Log: ", *args, **kwargs)

    def __call__(self, string, table):
        self.string = string
        self.table = table
        try:
            self.dataSet = pd.read_csv(self.table, encoding='utf-8', header=0)
        except IOError:
            print("The table isn't correct.")


def author(f):
    @functools.wraps(f)
    def decorator(*args, **kwargs):
        reader = functools.partial(open, encoding="utf-8", mode="r")
        file = reader("user.txt")
        user = [json.loads(line) for line in file.readlines()]
        count = 0
        while True:
            username = str(input("请输入登录用户: "))
            password = str(input("请输入登录密码: "))
            if count > 3:
                break
            if {"username": username, "password": password} not in user:
                print("Username or password not correct. Please try again.")
                count += 1
            else:
                return f(*args, **kwargs)
    return decorator


class TableHandler(object):
    """负责执行文件操作"""
    def __sql_handler(self, handler):
        while True:
            yield handler.sql_handler()
    @author
    def loop(self, table):
        """负责循环"""
        handler = SqlHandler()
        while True:
            string = str(input("%s SQL >>> " % time.strftime("%Y-%m-%d %X", time.localtime())))
            handler(string, table)
            next(self.__sql_handler(handler))




if __name__ == '__main__':
    tb = TableHandler()
    tb.loop('table.txt')
