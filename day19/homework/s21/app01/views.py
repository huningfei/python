from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from app01 import my_md5
from functools import wraps
from django.contrib import auth # 必须先导入auth
from django.contrib.auth.decorators import login_required #auth装饰器
from django.contrib.auth.models import User  # 创建用户auth自带

# 登录
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        next_url = request.GET.get("next")
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        user_obj = auth.authenticate(request, username=username, password=pwd)

        if user_obj:
            auth.login(request, user_obj)  # # 给该次请求设置了session数据，并在响应中回写cookie
            if next_url:
                return redirect(next_url)
            else:
                return redirect("/index/")
        else:
            return render(request, "login.html", {"error_msg": "用户名或密码错误"})

#首页
@login_required()
def index(request):
    user = request.user
    return render(request,"index.html",{"v":user})



# 注销页面
@login_required
def logout(request):
    # 删除所有当前请求相关的session
    request.session.delete()
    return redirect("/login/")

# 创建用户
def register_user(request):
    if request.method == "GET":
        return render(request, "register_user.html")
    else:
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        user_obj = User.objects.create_user(username=username, password=pwd)  # 用auth自带的去创建用户，这里用的是数据库自带的user表
        return redirect("/login/")
# 更改密码
# @login_required
# def change_password():















