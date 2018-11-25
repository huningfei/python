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


def login(request):
    """
    用户登录
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'login.html')

    user = request.POST.get('username')

    pwd = md5(request.POST.get('password'))

    user_object = models.UserInfo.objects.filter(username=user, password=pwd).first()

    if not user_object:
        return render(request, 'login.html', {'error': '用户名或密码错误'})
    # 用户登录的信息存储到session里面
    request.session['user_info'] = {'id': user_object.id, 'name': user_object.username}
    init_permission(user_object, request)


    return redirect(reverse('index'))


def index(request):
    return render(request, 'index.html')
