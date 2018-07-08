# -*- encoding:utf-8 -*-
import sys
import os
#生成器
def user_list_g():
    with open('user_list.txt',encoding='utf-8',mode='r') as f:
        data =[eval(i) for i in f]
    for i in data:
        yield i
#用户状态
login_status = False
#装饰器
def zsq(args):
    def inner():
        if login_status:
            args()
        else:
            print("请您先登录！！".center(60,'-'))
    return inner
# 登录
def login():
    print("提示，账号：123 密码：123".center(60,'!'))
    global login_status
    if login_status:
        print("您已登录！")
    else:
        count = 3
        while count:
            l_g = user_list_g()
            luser =input("请输入账号：")
            lpass = input("请输入密码：")
            for i in l_g:
                if luser == i.get('username') and lpass == i.get('passwd'):
                    login_status = True
            if login_status:
                print("登录成功！".center(60,'-'))
                break
            else:
                 print("账号密码错误！")
            count -=1
# 读文件
@zsq
def select1():
    with open('list', 'r', encoding='utf-8') as f:
        line = f.readlines()
        for i in line:
            print(i)
# 查
@zsq
def select():
    '''
    函数查询
    :return:
    '''
    print("功能提示".center(60,'~'))
    msg = '''
    1.select name,age from staff_table where age > 22
    2.select * from staff_table where dept = "IT"
    3.select * from staff_table where enroll_date like "133"
'''
    print(msg)
    print("功能提示".center(60,'~'))
    user_input = input('SQL>>>:').strip()
    user_inupt1 = user_input.split(' ')
    if user_input == 'select name,age from staff_table where age > %s' % (user_inupt1[7]):
        with open('list', 'r+', encoding='utf-8') as f:
            list1 = []
            count = 0
            for line in f:
                i = line.strip().split(',')
                if i[2] > user_inupt1[7]:
                    list1.append(i)
            for s in list1:
                count = count + 1
            for j in list1:
                print(j)
    elif user_input == ('select * from staff_table where dept = %s' % (user_inupt1[7])):
        with open('list', 'r', encoding='utf-8') as f:
            list2 = []
            count = 0
            for line in f:
                i1 = line.strip().split(',')
                if i1[4] == eval(user_inupt1[7]):
                    list2.append(i1)
                count = count + 1
            for j1 in list2:
                print(j1)
    elif user_input == ('select * from staff_table where enroll_date like %s' % (user_inupt1[7])):
        with open('list', 'r+', encoding='utf-8') as f:
            list3 = []
            list4 = []
            count = 0
            for line in f:
                i = line.strip().split(',')
                list3.append(i)
            for j in list3:
                m = j[4]
                if m[0] == eval(user_inupt1[7]):
                    list4.append(j)
            for s in list4:
                count = count + 1
                if count < 1:
                    print('没有找到类似条目！！！')
                    pass
                else:
                    pass
            for j in list4:
                print(j)
    return ()
# 曾
@zsq
def alter():
    '''
    添加函数
    :return:
    '''
    print("功能提示".center(60,'^'))
    msg = '''
    1)命令如：zs,24,13651054601,HR,
                    格式： 名字，年龄，电话，职业， （以逗号分隔！！）
    '''
    print(msg)
    print("功能提示".center(60, '^'))
    user_input = input('SQL>>>:')
    user_input1 = user_input.split(',')
    with open('list', 'r+', encoding='utf-8') as f:
        lists = []
        for line in f:
            s2 = line.strip().split(',')
            m = s2[3]
            lists.append(m)
        if user_input1[2] in lists:
            print('这条记录已经存在！！！')
            main()
        else:
            my_index = str(len(lists) + 1)
            user_input1.insert(0, my_index)
            user_input1 = ','.join(user_input1)
        f.flush()
        f.write(user_input1)
        f.write('\n')
        f.close()
        print("记录添加完成！！！", '\n')
    return ()
# 删
@zsq
def delect():
    '''
    删除函数
    :return:
    '''
    print("功能提示".center(60,'*'))
    print('-----请输入删除命令例如：输入用户ID 即可以从list中删除！')
    msg = '''
    1)按1删除、直接删除ID即可
    2)按2或者q退出
    '''
    print(msg)
    print("功能提示".center(60, '*'))
    user_input = input('SQL>>>:')
    if user_input == '1':
        print('现有的用户为：')
        select1()
        print('\n')
        user_input1 = input('请输入需要删除的用户ID:')
        user_input2 = user_input1[0]
        f = open('list', 'r+', encoding='utf-8')
        f1 = open('new_list', 'w+', encoding='utf-8')
        for line in f:
            i = line.strip().split(',')
            i1 = i[0]
            if user_input2 != i1:
                i = ','.join(i)
                f1.write(i)
                f1.write('\n')
            else:
                continue
        f.close()
        f1.close()
        os.remove('list')
        os.rename('new_list', 'list')
        print('\n')
        select1()
    elif user_input == '2' or 'q':
        sys.exit()
    return
# 更新
@zsq
def update():
    '''
    更新函数
    :return:
    '''
    msg = '''
    1)这里第一个等号按照没有空格的格式划分
    2)命令范例:UPDATE staff_table SET dept="INS" where dept = "HR"
    '''
    print(msg)
    user_choice_input = input('SQL>>>:')
    user_choice_input1 = user_choice_input.split(' ')
    dept = user_choice_input1[3].split('=')
    dept_new = dept[1]
    dept_old = user_choice_input1[7]
    if user_choice_input == ('UPDATE staff_table SET dept=%s where dept = %s' % (dept_new, dept_old)):
        dept_new1 = eval(dept_new)
        dept_old1 = eval(dept_old)
        f = open('list', 'r+', encoding='utf-8')
        f1 = open('new_list', 'w+', encoding='utf-8')
        for line in f:
            i = line.strip().split(',')
            dept_change = i[4]
            if dept_change == dept_old1:
                i[4] = eval(dept_new)
            i = ','.join(i)
            f1.write(i)
            f1.write('\n')
        f.close()
        f1.close()
        os.remove('list')
        os.rename('new_list', 'list')
        print('\n')
        select1()
        pass
    return ()
# 交互
def main():
    '''
    交互
    :return:
    '''
    print('员工信息选择'.center(60,'*'))
    msg = '''
        1、登录 2、查询 3、添加 4、删除 5、更新 6、退出
  '''
    exit_fiag = False
    while not exit_fiag:
        print(msg)
        user_choice = input('请选择>>>:').strip()
        if user_choice == '2':
            select()
        elif user_choice == '3':
            alter()
        elif user_choice == '4':
            delect()
        elif user_choice == '5':
            update()
        elif user_choice == '6':
            sys.exit()
        elif user_choice == '1':
            login()
        else:
            print('输入错误!，请重新输入！！！')
            main()

main()