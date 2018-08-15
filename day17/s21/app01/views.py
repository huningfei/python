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
                request.session.set_expiry(0) # 设置过期时间，浏览器关闭就失效
                request.session['user'] = obj.username # 获取的登录的用户名
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

            return render(request, "add_user.html", {"v": v})
        else:
            return redirect("/login/")


# 主机管理
# 查看
def show_host(request):
    v = request.session.get('user')
    if v:
        host_list = models.Host.objects.all()
        return render(request, "host/show_host.html", {"host_list": host_list,"v":v})
    else:
        return redirect("/login/")


# # 增加
def add_host(request):
    if request.method == "POST":
        name = request.POST.get("hostname")
        password = request.POST.get("password")
        id = request.POST.get("service")
        if name == "" or password == "":
            data = "主机名或密码不能为空"
            return render(request, "host/add_host.html", {"data": data})

        else:
            old_name = models.Host.objects.filter(hostname=name)
            if old_name:
                data = "主机名已存在"
                return render(request, "host/edit_host.html", {"data": data})
            else:
                models.Host.objects.create(hostname=name, service_id=id, pwd=password)

            return redirect("/show_host/")
    else:
        v = request.session.get('user')
        if v:
            host = models.Service.objects.all()
            return render(request, "host/add_host.html", {"host_list": host,"v":v})
        else:
            return redirect("/login/")


# 编辑
def edit_host(request, pk):
    if request.method == "GET":
        v = request.session.get('user')
        if v:
        # 获取机器id
            host_id = models.Host.objects.get(id=pk)
            service_obj = models.Service.objects.all()
            return render(request, "host/edit_host.html", {"host": host_id, "service_list": service_obj,"v":v})
        else:
            return redirect("/login/")

    else:
        # 获取机器id
        host_id = models.Host.objects.get(id=pk)
        # 获取主机名
        new_hostname = request.POST.get("hostname")
        # 获取密码
        new_pwd = request.POST.get("password")
        # 获取所在业务名称
        new_service_id = request.POST.get("service")
        # 更改
        host_id.hostname = new_hostname
        host_id.pwd = new_pwd
        host_id.id = new_service_id
        old_name = models.Host.objects.filter(hostname=new_hostname)
        if old_name:
            data = "主机名已存在"
            return render(request, "host/edit_host.html", {"data": data})
        else:
            host_id.save()
        return redirect("/show_host/")


# 删除主机
def del_host(request, pk):
    if request.method == "GET":
        models.Host.objects.get(id=pk).delete()
        return redirect("/show_host/")
