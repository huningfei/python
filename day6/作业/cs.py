




def student_view(): #学生视图
    choice_id = input("\n*************************学生功能********************\n"
                      "0.查看班级"
                      "1.查看课程")

    # if choice_id =='0':
    #     schoolid.show_class()
    # elif choice_id == '1':
    #     schoolid.show_course()
def teacher_view(): #老师视图
    choice_id = input("\n*************************讲师功能********************\n"
                      "0.查看班级"
                      "1.查看课程")

user_status = {
    'username': None,
    'status': False
}

username = input("\033[1;33m请输入你的用户名:\033[0m")
password = input("\033[1;33m请输入你的密码:\033[0m")
with open(r'C:\python21\day6\作业\db\info',encoding='utf-8')as f1:
    for i in f1:
        a = (i.split())

        if a[0] == username and a[1] == password and a[2] == 'student':
            user_status['status'] = True
            student_view()
            print("\033[1;33m登录成功\033[0m")
        elif a[0] == username and a[1] == password and a[2] =='teacher':
            user_status['status'] = True
            teacher_view()
