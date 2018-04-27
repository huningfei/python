from prettytable import PrettyTable  ##导入可以打印表格的模块

##转换数据
TITLE=['id','name','age','phone','job']
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
#print(dic)

def gt(a,b):
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

    '''
    :param a: age
    :param b: 22
    :return:
    '''

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
    for index, val in enumerate(dic[a]):  ##age[22,23,]并求出age的各个索引
        if val == b:  ##匹配上了
            # print("match",val)
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
    # print("查询到的数据:",match_list)
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
            a,b = right_yuju.split(fu_hao)#a和b接受到了age和22
            matched_data = value(a.strip(),b.strip())
            #print(matched_data)
            return matched_data

    else:
        print('where语法错误')
    ''' 
    解析where条件，判断大于，小于，等于和like
    :return: age>22
    '''
def check_input(cmd):  ## 检测输入的语句，并分割成两个语句（cmd是从用户输入的命令传过来的）
    syntax_list={
        'select':select,
        'update':update,
        'add':add,
        'delete':delete

    }
    if cmd.split()[0] in ('select','update','delete','insert'):#取出用户输入的第一个命令
        left_yuju,right_yuju = cmd.split('where')#以where关键字分割语句
        # print(left_yuju,right_yuju)
        matched_data=check_where(right_yuju)#把where后面的语句传送给了check_where
        cmd_action=left_yuju.split()[0] ##获取是4个语句中的那个
        if cmd_action in syntax_list:
            syntax_list[cmd_action](matched_data,left_yuju)
    else:
        print("语法错误")



def where():
    pass

def select(match_data,left_yuju):

    '''
    :param match_data: [['2', 'Egon', '23', '13304320533', 'Tearcher\n'], ['3', 'nezha', '25', '1333235322', 'IT']]
    :param left_yuju: elect name, age 左边的语句
    :return:
    '''


def update():
    pass

def delete():
    pass

##输入语句
def yuju():
    while True:
        cmd =  input("mysql>>:").strip()
        if not cmd:
            continue
        check_input(cmd) ##传给检测你输入语句的函数
yuju()


    # query = input('请输入你的sql语句>>>:').strip()
    # if 'select' in query:
    #     select()
    # elif 'update' in query:
    #     update()
    # elif 'update' in query:
    #     delete()
    # else:
    #     print("语法错误")
