from functools import wraps
from django.shortcuts import render, HttpResponse, redirect



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