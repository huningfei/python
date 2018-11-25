from django.shortcuts import render, redirect
from django.urls import reverse
from crm import models
from crm.pwd.md5 import md5
from rbac.service.permission import init_permission
from functools import wraps


# session 登录装饰器
def login_check(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        next_url = request.path_info

        if request.session.get('user'):
            return func(request, *args, **kwargs)
        else:
            return redirect("/login/?next_url={}".format(next_url))

    return inner


# 注销页面
@login_check
def logout(request):
    # 删除所有当前请求相关的session
    request.session.delete()
    return redirect("/login/")



