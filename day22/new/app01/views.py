from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from rbac.service.permission import init_permission
from rbac.models import UserInfo


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pwd = request.POST.get("password")

        user_obj = UserInfo.objects.filter(username=username, password=pwd).first()
        if user_obj:
            # 登录成功
            # 初始化权限信息
            init_permission(request, user_obj)
            return redirect("/book_list/")
    return render(request, "login.html")


def book_list(request):
    return render(request, "book_list.html")


def book_add(request):
    return render(request, "book_add.html")
