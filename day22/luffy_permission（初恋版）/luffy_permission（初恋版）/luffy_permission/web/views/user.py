'''
跟用户相关的视图都写在这里
'''
from django.shortcuts import redirect,render,HttpResponse
from rbac.models import UserInfo
from django.conf import settings

def login(request):
    error_msg=""
    if request.method=="POST":
        # 取用户名和密码
        username=request.POST.get("username")
        pwd=request.POST.get("password")
        #验证
        user_obj=UserInfo.objects.filter(username=username,password=pwd).first()
        if user_obj:
            #登录成功
            #user_obj.roles.all()那到当前用户的所有角色
            ret=user_obj.roles.all().values("permissions__url",
                                            "permissions__icon",
                                            "permissions__is_menu",
                                            "permissions__title"
                                            ).distinct() # 取到去重之后的权限
            # 定义一个权限列表
            permission_list=[]
            #定义一个专门用来存放当前用户菜单的列表
            menu_list=[]
            for item in ret:
                print(item) #item是个大列表
                permission_list.append({"permissions__url":item["permissions__url"]}) #添加到权限列表
                if item["permissions__is_menu"]: # 如果为真
                    menu_list.append({
                        "title":item["permissions__title"],
                        "icon":item["permissions__icon"],
                        "url":item["permissions__url"]
                    })

            # 将用户权限列表信息，存到session中
            request.session[settings.PERMISSION_SESSION_KEY]=permission_list
            # 把当前用户的所有菜单存放到sessioin
            request.session[settings.MENU_SESSION_KEY]=menu_list
            return redirect("/customer/list/")
        else:
            error_msg="用户名或密码错误"


    return render(request,"login.html")