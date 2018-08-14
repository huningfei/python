from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from app01 import my_md5


# 登录页面
#
def login(request):
    if request.method == "POST":
        user = request.POST.get("username")  # 这里的username必须和html里面的name的值一致
        pwd = request.POST.get("password")
        if user == "" or pwd == "":
            data = '用户名或密码不能为空'
            return render(request, "login.html", {"data": data})
        else:
            try:
                obj = models.User.objects.get(username=user)
            except Exception:
                data = "此用户不存在"
                return render(request, "login.html", {"data": data})

            if obj.username == user and obj.password == my_md5.md5(user, pwd):
                request.session.set_expiry(0)
                request.session['user'] = obj.username
                return redirect("/show_user/")

            else:

                data = '用户名和密码错误'
                return render(request, "login.html", {"data": data})
    else:
        return render(request, 'login.html')


# 展示页面

def show_user(request):
    data = models.User.objects.all()
    v = request.session.get('user')  # 获取登录的用户名
    if v:
        return render(request, "show_user.html", {"data": data, "v": v})
    else:
        return redirect('/login/')


# 注册页面
def register_user(request):
    if request.method == "POST":
        # 获取用户添加的用户名和密码
        user = request.POST.get("username")
        pwd = request.POST.get("password")
        if user == "" or pwd == "":
            # return HttpResponse("用户名和密码不能为空")
            data = '用户名和密码不能为空'
            return render(request, "register_user.html", {"data": data})
        else:
            # 写入到数据库
            try:
                models.User.objects.create(username=user, password=my_md5.md5(user, pwd))
            except Exception:
                data = '用户名已经存在'
                return render(request, "register_user.html", {"data": data})
            data = '注册成功,请登录'

            return render(request, "register_user.html", {"data": data})
    else:

        return render(request, "register_user.html")


# 删除用户
def del_user(request):
    # 获取用户要删除的id
    del_id = request.GET.get("id")
    # 去数据库里面删除
    models.User.objects.get(id=del_id).delete()
    # 返回展示页面

    return redirect("/show_user/")


# 编辑用户
def edit_user(request):
    if request.method == "POST":
        edit_id = request.POST.get("id")
        new_user = request.POST.get("username")
        new_pwd = request.POST.get("password")
        obj = models.User.objects.get(id=edit_id)
        obj.username = new_user
        obj.password = my_md5.md5(new_user, new_pwd)

        try:
            obj.save()
        except Exception:
            data = '用户名已经存在'
            return render(request, "edit_user.html", {"data": data})
        return redirect("/show_user/")

    else:
        edit_id = request.GET.get("id")
        obj = models.User.objects.get(id=edit_id)
        v = request.session.get('user')
        if v:
            # 把要编辑的用户展示在这个页面上面
            return render(request, "edit_user.html", {"user": obj, "v": v})
        else:
            return redirect("/login/")
def add_user(request):
    if request.method == "POST":
        # 获取用户添加的用户名和密码
        user = request.POST.get("username")
        pwd = request.POST.get("password")
        if user == "" or pwd == "":
            data = '用户名和密码不能为空'
            return render(request, "add_user.html", {"data": data})
        else:
            # 写入到数据库
            try:
                models.User.objects.create(username=user, password=my_md5.md5(user, pwd))
            except Exception:
                data = '用户名已经存在'
                return render(request, "add_user.html", {"data": data})
            return redirect("/show_user/")
    else:
        v = request.session.get('user')
        if v:

            return render(request, "add_user.html",{"v":v})
        else:
            return redirect("/login/")

# 主机管理
# 查看
def show_host(request):
    host_list=models.Host.objects.all()
    return render(request,"./host/show_host.html",{"host_list":host_list})
# # 增加
# def add_host(request):
