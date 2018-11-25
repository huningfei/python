from django.shortcuts import render, HttpResponse, redirect
from rbac.service.permission import init_permission
from rbac import models


def login(request):
    """
    用户登录
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, 'app01/login.html')

    user = request.POST.get('user')
    pwd = request.POST.get('pwd')

    user = models.UserInfo.objects.filter(username=user, password=pwd).first()
    if not user:
        return render(request, 'app01/login.html', {'msg': '用户名或密码错误'})
    init_permission(user, request)

    return redirect('/app01/user/')


def user_list(request):
    """
    用户列表
    :param request:
    :return:
    """
    user_queryset = [
        {'id': '1', 'name': '王振兴'},
        {'id': '2', 'name': '高栋'},
        {'id': '3', 'name': '乔瑞武'},
    ]

    return render(request, 'app01/user_list.html', {'user_queryset': user_queryset})


def user_add(request):
    return render(request, 'app01/user_add.html')


def user_edit(request, nid):
    return render(request, 'app01/user_edit.html')


def user_del(request, nid):
    return HttpResponse('删除成功')


def center(request):
    return render(request, 'app01/center.html')
