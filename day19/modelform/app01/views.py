from django.shortcuts import render, redirect
from app01 import models
from app01.forms import BookModelForm
from django.contrib.auth.decorators import login_required  # auth自带的装饰器
from django import views

# Create your views here.
def book_list(request):
    data = models.Book.objects.all()
    return render(request, "book_list.html", {"data": data})


@login_required
def add_book(request):
    form_obj = BookModelForm()
    if request.method == "POST":
        form_obj = BookModelForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect("/book_list/")
    return render(request, "add_book.html", locals())


def edit_book(request, pk):
    book_obj = models.Book.objects.filter(id=pk).first()
    print("我是book_obj", book_obj)
    # instance实例
    form_obj = BookModelForm(instance=book_obj)  # 实例化的form_obj
    if request.method == "POST":
        # 获取用户提交过来的数据，用request.POST传过来的数据去更新book_obj这本书
        form_obj = BookModelForm(request.POST, instance=book_obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect("/book_list/")
    return render(request, "edit_book.html", locals())


from django.contrib import auth


# 登录
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        next_url = request.GET.get("next")
        print(next_url)
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        user_obj = auth.authenticate(request, username=username, password=pwd)
        if user_obj:
            auth.login(request, user_obj)  # # 给该次请求设置了session数据，并在响应中回写cookie
            if next_url:
                return redirect(next_url)
            else:
                return redirect("/book_list/")
        else:
            return render(request, "login.html", {"error_msg": "用户名或密码错误"})


from django.contrib.auth.models import User  # 创建用户auth自带


def reg(request):
    if request.method == "GET":
        return render(request, "reg.html")
    else:
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        user_obj = User.objects.create_user(username=username, password=pwd)  # 用auth自带的去创建用户
        return redirect("/login/")
# class RegView(views.View):
#     def get(self, request):
#         return render(request, "reg.html")
#
#     def post(self, request):
#         username = request.POST.get("username")
#         pwd = request.POST.get("password")
#         # 去数据库中创建用户
#         # User.objects.create()  --> 直接在数据库创建用户，密码是存的明文的
#         user_obj = User.objects.create_user(username=username, password=pwd)
#         # User.objects.create_superuser()  # 创建的超级用户
#         return redirect("/login/")