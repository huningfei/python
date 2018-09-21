'''
跟用户相关的视图都写在这里
'''
from django.shortcuts import redirect, render, HttpResponse
from rbac.models import UserInfo
from rbac.service.permission import init_permission


def login(request):
    error_msg = ""
    if request.method == "POST":
        # 取用户名和密码
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        # 验证
        user_obj = UserInfo.objects.filter(username=username, password=pwd).first()
        if user_obj:
            # 登录成功
            # 调用封装好的初始化函数里面含有权限列表和显示菜单
            init_permission(request,user_obj)

            return redirect("/customer/list/")
        else:
            error_msg = "用户名或密码错误"

    return render(request, "login.html",locals())
