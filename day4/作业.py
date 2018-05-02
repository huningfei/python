import os

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
print(dic)

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
        if str(val) == str(b):  ##匹配上了
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
    if filter_cols==['*']:
        #reformat_data_set = []  ##最终要打印的数据
        for row in match_data:  ##row是['3', 'nezha', '25', '1333235322', 'IT']
            filtered_vals = []  ##['Egon', '23']  ['nezha', '25']
            for col in TITLE:  ##col是name和age
                #print(col)
                col_index = TITLE.index(col)  ##name和age在title里面的索引1和2的位置
                filtered_vals.append(row[col_index])  # ['3', 'nezha', '25', '1333235322', 'IT'][1]
            #print(filtered_vals)
            reformat_data_set.append(filtered_vals)
        print(reformat_data_set)

    else:
        for row in match_data: ##row是['3', 'nezha', '25', '1333235322', 'IT']
            filtered_vals=[]  ##['Egon', '23']  ['nezha', '25']
            for col in filter_cols: ##col是name和age
                col_index = TITLE.index(col) ##name和age在title里面的索引1和2的位置
                filtered_vals.append(row[col_index])#['3', 'nezha', '25', '1333235322', 'IT'][1]
            reformat_data_set.append(filtered_vals)
        print(reformat_data_set)



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
    if cmd.split()[0] in ('select','update','delete','insert'):#取出用户输入的第一个命令
        left_yuju,right_yuju = cmd.split('where')#以where关键字分割语句
        matched_data=check_where(right_yuju)#把where后面的语句传送给了check_where
        #print(matched_data)
        syntax_list[cmd.split()[0]](matched_data,left_yuju)  #  select update inst select() res = dic
        # update_file(res)
    else:
        print("语法错误")

def insert(cmd):
    pass

def update(match_data,left_yuju):
    '''
        :param match_data: ['3', 'nezha', '25', '1333235322', 'IT'] ['4', 'hnf', '25', '1333235322', 'IT']
        :param left_yuju: update name='bob' from  userinfo
        :return:
        '''
    filter_cols = left_yuju.split('from')[0].split()[1].split('=') #取出['name', 'bob']
    for line in match_data:
        line_id = line[0] #取出id
        index = dic["id"].index(line_id)##取出id在上面字典里的索引
        dic[filter_cols[0]][index] = filter_cols[1] #dic[filter_cols[0]] #获取出所有的名字，然后在获取名字对应的索引
        update_file(dic)
        #return dic

def delete():
    pass
#
def update_file(update):
    list_id = dic.get('id')
    list_name = dic.get('name')
    list_age = dic.get('age')
    list_phone = dic.get('phone')
    list_job = dic.get('job')
    a = zip(list_id, list_name,list_age, list_phone, list_job)
    for i in a:
        with open("userinfo.bak", "a", encoding="utf-8") as f1:
                str_i = ",".join(i)
                print(str_i)
                f1.write(str_i)
    os.remove("userinfo")
    os.rename('userinfo.bak','userinfo')

##输入语句
def yuju():
    while True:
        cmd =  input("mysql>>:").strip()
        if not cmd:
            continue
        check_input(cmd) ##传给检测你输入语句的函数
yuju()