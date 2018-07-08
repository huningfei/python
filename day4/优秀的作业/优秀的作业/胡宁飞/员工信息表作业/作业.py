##博客 http://www.cnblogs.com/huningfei/p/8931518.html
## http://www.cnblogs.com/huningfei/p/8920759.html
import os
from tabulate import tabulate#安装打印模块的表格
##打印支持的语句
with open('sentence',encoding='utf-8',mode='r')as f1:
    print('\033[1;33m目前支持的语句有: \n %s\033[0m' % f1.read())

TITLE=['id','name','age','phone','job']
def zhuanhan():##转换数据
    with open('userinfo',encoding='utf-8',mode='r') as f1:
        dic = {}
        for i in TITLE:
            dic[i] = []
        #print(dic)
        for line in f1:
            pid,name,age,phone,job = line.split(",")
            dic['id'].append(pid)
            dic['name'].append(name)
            dic['age'].append(age)
            dic['phone'].append(phone)
            dic['job'].append(job)
    return dic

def gt(a,b):
    '''
     :param a: age
     :param b: 22
     :return:
     '''
    match_list =[]
    for index,val in enumerate(dic[a]): ##age[22,23,]并求出age的各个索引
        if int(val) > int(b): ##匹配上了
            # print("match",val)
            onwer_list=[]
            for col in TITLE:
                onwer_list.append(dic[col][index])
            match_list.append(onwer_list)
    #print("查询到的数据:",match_list)
    return match_list



def lt(a,b):
    match_list = []
    for index, val in enumerate(dic[a]):  ##age[22,23,]并求出age的各个索引
        if int(val) < int(b):  ##匹配上了
            # print("match",val)
            onwer_list = []
            for col in TITLE:
                onwer_list.append(dic[col][index])
            match_list.append(onwer_list)
    # print("查询到的数据:",match_list)
    return match_list

def eq(a,b):
    match_list = []
    for index, val in enumerate(dic[a]):  ##a代表age , age[22,23,]并求出age的各个索引
        if str(val.strip()) == str(b.strip()):  ##匹配上了
            onwer_list = []
            for col in TITLE:
                onwer_list.append(dic[col][index])
            match_list.append(onwer_list)
    # print("查询到的数据:",match_list)
    return match_list
def op_like(a,b):
    match_list = []
    for index, val in enumerate(dic[a]):  ##age[22,23,]并求出age的各个索引
        if b in val:  ##匹配上了
            # print("match",val)
            onwer_list = []
            for col in TITLE:
                onwer_list.append(dic[col][index])
            match_list.append(onwer_list)

    return match_list


def check_where(right_yuju):
    tiaojian = {
        '>':gt,
        '<':lt,
        '=':eq,
        'like':op_like,
    }
    for fu_hao,value in tiaojian.items():
        #print(value)
        if fu_hao in right_yuju:
            a,b = right_yuju.split(fu_hao)#a和b接受到了age和22 a是key b是value
            matched_data = value(a.strip(),b.strip())
            #print(matched_data)
            return matched_data

    else:
        print('where语法错误')
    ''' 
    解析where条件，判断大于，小于，等于和like
    :return: age>22
    '''
def select(match_data,left_yuju):
    """
    ##这个只是可以查看name和age的语句
    :param match_data:[['2', 'Egon', '23', '13304320533', 'Tearcher\n'], ['3', 'nezha', '25', '1333235322', 'IT']]
    :param left_yuju: select name, age  from userinfo
    :return:
    """

    filter_cols_tmp = left_yuju.split('from')[0].split()[1:] #取出name,和age 例：[' name', ' age ']
    filter_cols = [i.strip().strip(",") for i in filter_cols_tmp] ##取出干净的name和age
    reformat_data_set = []  ##最终要打印的数据
    if "*" in filter_cols:
        filter_cols = TITLE  # [id,age,name,phone,job]
        for row in match_data: ##row是['3', 'nezha', '25', '1333235322', 'IT']
            filtered_vals=[]  ##['Egon', '23']  ['nezha', '25']
            for col in filter_cols: ##col是name和age
                col_index = TITLE.index(col) ##name和age在title里面的索引1和2的位置
                filtered_vals.append(row[col_index])#['3', 'nezha', '25', '1333235322', 'IT'][1]
            reformat_data_set.append(filtered_vals)
        print(tabulate(reformat_data_set, headers=TITLE, tablefmt="grid"))
    else:
        # filter_cols = TITLE  # [id,age,name,phone,job]
        for row in match_data:  ##row是['3', 'nezha', '25', '1333235322', 'IT']
            filtered_vals = []  ##['Egon', '23']  ['nezha', '25']
            for col in filter_cols:  ##col是name和age
                col_index = TITLE.index(col)  ##name和age在title里面的索引1和2的位置
                filtered_vals.append(row[col_index])  # ['3', 'nezha', '25', '1333235322', 'IT'][1]
            reformat_data_set.append(filtered_vals)
        print(tabulate(reformat_data_set, headers=TITLE, tablefmt="grid"))

def check_input(cmd):  ## 检测输入的语句，并分割成两个语句（cmd是从用户输入的命令传过来的）
    """
    :param cmd: select name, age where age>22
    :return:
    """
    syntax_list={
        'select':select,
        'update':update,
        'add':insert,
        'delete':delete

    }
    if 'where' not in cmd and 'insert' not in cmd:## 这个是select * from userinfo 查询所有
        zhuanhan()
        print(tabulate(dic, headers=TITLE, tablefmt="grid"))
    else:
        if cmd.split()[0] in ('select','update','delete',):#取出用户输入的第一个命令
            left_yuju,right_yuju = cmd.split('where')#以where关键字分割语句
            matched_data=check_where(right_yuju)#把where后面的语句传送给了check_where
            #print(matched_data)
            syntax_list[cmd.split()[0]](matched_data,left_yuju)  #  select update inst select() res = dic
            # update_file(res)
        elif cmd.split()[0] == 'insert':
            insert(cmd)
        else:
            print("语法错误")

def insert(cmd):
    '''

    :param cmd: 如：insert into userinfo id,name,age,phone,job values 5,jinxing,43,123456789,python
    :return:
    '''
    filter_values = cmd.split('values')[-1].split(',')  ##5,jinxing,43,123456789,python
    insert_file(filter_values)

def update(match_data,left_yuju):
    '''
        :param match_data: ['3', 'nezha', '25', '1333235322', 'IT'] ['4', 'hnf', '25', '1333235322', 'IT']
        :param left_yuju: update name='bob' from  userinfo
        :return:
        '''
    print('影响了%s行' %(len(match_data)))
    filter_cols = left_yuju.split('from')[0].split()[1].split('=') #取出['name', 'bob']
    for line in match_data:
        line_id = line[0] #取出id
        index = dic["id"].index(line_id)##取出id在上面字典里的索引
        dic[filter_cols[0]][index] = filter_cols[1] #dic[filter_cols[0]] #获取出所有的名字，然后在获取名字对应的索引
        update_file(dic)
        #return dic

def delete(match_data,left_yuju):
    print('影响了%s行' %(len(match_data)))
    filter_cols = left_yuju.split('from')[0].split()[1].split('=')
    for del_line in match_data:
        line_id = del_line[0]  # 取出id
        index = dic["id"].index(line_id)  ##取出id在上面字典里的索引
        dic.get("id").pop(index)
        dic.get("name").pop(index)
        dic.get("age").pop(index)
        dic.get("phone").pop(index)
        dic.get("job").pop(index)
        #print(dic)
        delete_file(dic)
def insert_file(filter_values):

    '''
    :param filter_values: [6, 'hnf', '23', '123456789', 'python']
    :return:
    '''
    global dic
    with open('userinfo', encoding='utf-8', mode='a+') as f1:

        n = 0
        for i in filter_values:
            n += 1
            if n == 1:
                i = int(dic.get('id')[-1]) + 1
                f1.write(str(i)+',')
            elif 1< n < 5:
                f1.write(i.strip() + ',')
            else:
                f1.write(i + "\n")
                print("添加完毕")
                f1.seek(2)


def delete_file(dic):
    '''

    :param dic:从文件读取的数据{'id': ['1', '2', '3'], 'name': ['Alex', 'Egon', 'wusir'], 'age': ['23', '24', '35'], 'phone': ['13651054608', '13304320533', '1333235322'], 'job': ['IT\n', 'Tearcher\n', 'IT']}
    :return:
    '''
    list_id = dic.get('id')
    list_name = dic.get('name')
    list_age = dic.get('age')
    list_phone = dic.get('phone')
    list_job = dic.get('job')
    list_data = zip(list_id, list_name, list_age, list_phone, list_job)
    for i in list_data:
       with open('userinfo.bak',encoding='utf-8',mode="a")as f1:
           str_i=",".join(i)
           #print(str_i)
           f1.write(str_i)
    os.remove('userinfo')
    os.rename("userinfo.bak","userinfo")
def update_file(dic):
    list_id = dic.get('id')
    list_name = dic.get('name')
    list_age = dic.get('age')
    list_phone = dic.get('phone')
    list_job = dic.get('job')
    a = zip(list_id, list_name,list_age, list_phone, list_job)
    for i in a:
        with open("userinfo.bak", "a", encoding="utf-8") as f1:
                str_i = ",".join(i)
                #print(str_i)
                f1.write(str_i)

    os.remove("userinfo")
    os.rename('userinfo.bak','userinfo')

##输入语句
def yuju():
    while True:
        global dic
        dic = zhuanhan()
        cmd = input("mysql>>:").strip()#cmd就是指用户开始输入的语句
        if not cmd:
            continue
        check_input(cmd) ##传给检测你输入语句的函数

yuju()