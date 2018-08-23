from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from app01 import my_md5
from functools import wraps
from app01 import mypage



# session 登录装饰器
def login_check(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        next_url = request.path_info
        # print(path)
        # next_url=request.get_full_path()
        # print("next_url第一个", next_url)
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

# 登录页面
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
                request.session.set_expiry(0)  # 设置过期时间，浏览器关闭就失效
                request.session['user'] = obj.username  # 获取的登录的用户名
                next_url=request.GET.get("next_url") # 获取url后面拼接的路径
                # print(next_url) #结果为空
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect("/show_user/")

            else:

                data = '用户名和密码错误'
                return render(request, "login.html", {"data": data})
    else:
        return render(request, 'login.html')


# 展示页面
@login_check
def show_user(request):
    current_user = request.session.get("user", None)  # 获取用户名
    data = models.User.objects.all()
    total_count=data.count()
    current_page=request.GET.get("page")
    page_obj = mypage.MyPage(current_page, total_count, url_prefix="show_user")
    range = data[page_obj.start:page_obj.end]  # 从开始到结束
    page_html = page_obj.page_html()
    page_num = page_obj.num()

    return render(request, "user/show_user.html", {"v": current_user, "data": range,"page_html":page_html,"num":page_num})


# 注册页面
def register_user(request):
    if request.method == "POST":
        # 获取用户添加的用户名和密码
        user = request.POST.get("username")
        pwd = request.POST.get("password")
        if user == "" or pwd == "":
            # return HttpResponse("用户名和密码不能为空")
            data = '用户名和密码不能为空'
            return render(request, "user/register_user.html", {"data": data})
        else:
            # 写入到数据库
            try:
                models.User.objects.create(username=user, password=my_md5.md5(user, pwd))
            except Exception:
                data = '用户名已经存在'
                return render(request, "user/register_user.html", {"data": data})
            data = '注册成功,请登录'

            return render(request, "user/register_user.html", {"data": data})
    else:

        return render(request, "user/register_user.html")


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
            return render(request, "user/edit_user.html", {"data": data})
        return redirect("/show_user/")

    else:
        edit_id = request.GET.get("id")
        obj = models.User.objects.get(id=edit_id)
        v = request.session.get('user')
        if v:
            # 把要编辑的用户展示在这个页面上面
            return render(request, "user/edit_user.html", {"user": obj, "v": v})
        else:
            return redirect("/login/")


# 增加用户
@login_check
def add_user(request):
    if request.method == "POST":
        # 获取用户添加的用户名和密码
        user = request.POST.get("username")
        pwd = request.POST.get("password")
        if user == "" or pwd == "":
            data = '用户名和密码不能为空'
            return render(request, "user/add_user.html", {"data": data})
        else:
            # 写入到数据库
            try:
                models.User.objects.create(username=user, password=my_md5.md5(user, pwd))
            except Exception:
                data = '用户名已经存在'
                return render(request, "user/add_user.html", {"data": data})
            return redirect("/show_user/")
    else:
        v = request.session.get('user')
        if v:

            return render(request, "user/add_user.html", {"v": v})
        else:
            return redirect("/login/")


# #############################################################主机管理
# 查看
@login_check
def show_host(request):
    current_user = request.session.get("user", None)  # 获取用户名
    data = models.Host.objects.all()
    total_count=data.count() #总数据
    current_page=request.GET.get("page") # 从浏览器获取页码
    #分页功能
    page_obj=mypage.MyPage(current_page, total_count, url_prefix="show_host")
    range=data[page_obj.start:page_obj.end] # 从开始到结束
    page_html=page_obj.page_html()
    page_num=page_obj.num()

    return render(request, "host/show_host.html", {"v": current_user, "host_list": range,"page_html":page_html,"num":page_num})


# # 增加
@login_check
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
            return render(request, "host/add_host.html", {"host_list": host, "v": v})
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
            return render(request, "host/edit_host.html", {"host": host_id, "service_list": service_obj, "v": v})
        else:
            return redirect("/login/")

    else:
        # 获取机器对象
        host_obj = models.Host.objects.get(id=pk)

        # 获取主机名
        new_hostname = request.POST.get("hostname")
        # print(new_hostname)
        # 获取密码
        new_pwd = request.POST.get("password")
        # 获取所在业务名称
        new_service_id = request.POST.get("service")

        # 更改
        host_obj.hostname = new_hostname
        host_obj.pwd = new_pwd
        host_obj.service_id = new_service_id
        old_name = models.Host.objects.filter(hostname=new_hostname)
        # if old_name:
        #     data = "主机名已存在"
        #     return render(request, "host/edit_host.html", {"data": data})
        # else:
        host_obj.save()
        return redirect("/show_host/")


# 删除主机
def del_host(request, pk):
    if request.method == "GET":
        models.Host.objects.get(id=pk).delete()
        return redirect("/show_host/")

###########################################################################业务管理
# 展示
@login_check
def show_service(request):
    current_user = request.session.get("user", None)  # 获取用户名
    data=models.Service.objects.all()
    total_count=data.count()
    current_page=request.GET.get("page")
    page_obj = mypage.MyPage(current_page, total_count, url_prefix="show_service")
    range = data[page_obj.start:page_obj.end]  # 从开始到结束
    page_html = page_obj.page_html()
    page_num = page_obj.num()


    return render(request,".//service/show_service.html",{"service_obj":range,"v":current_user,"page_html":page_html,"num":page_num})
# 增加业务
@login_check
def add_service(request):
    if request.method == "POST":

        service = request.POST.get("name")

        if service == "":
            data = '业务名称不能为空'
            return render(request, "service/add_service.html", {"data": data})
        else:
            # 写入到数据库
            try:
                models.Service.objects.create(name=service)
            except Exception:
                data = '业务名称已经存在'
                return render(request, "service/add_service.html", {"data": data})
            return redirect("/show_service/")
    else:
        v = request.session.get('user')
        if v:

            return render(request, "service/add_service.html", {"v": v})
        else:
            return redirect("/login/")

# 编辑业务
@login_check
def edit_service(request, pk):
    if request.method == "GET":
        v = request.session.get('user')
        if v:
            # 获取业务id
            service_id = models.Service.objects.get(id=pk)

            return render(request, "service/edit_service.html", {"service_obj": service_id, "v": v})
        else:
            return redirect("/login/")

    else:
        # 获取机器对象
        service_obj = models.Service.objects.get(id=pk)

        # 获取业务名称
        new_service = request.POST.get("name")

        # 更改
        service_obj.name = new_service
        old_name = models.Service.objects.filter(name=new_service)
        if old_name:
            data = "业务名已存在"
            return render(request, "service/edit_service.html", {"data": data})
        else:
            service_obj.save()
        return redirect("/show_service/")

# 删除业务
def del_service(request,pk):
    if request.method=="GET":
        models.Service.objects.filter(id=pk).delete()
        return redirect("/show_service/")
    
    
# 用户和业务关系############################################################################
# 展示页面
@login_check
def user_service_list(request):
    current_user = request.session.get("user", None)
    user=models.User.objects.all()
    total_count=user.count()
    current_page=request.GET.get("page")

    page_obj=mypage.MyPage(current_page,total_count,url_prefix="user_service_list")
    range = user[page_obj.start:page_obj.end]  # 从开始到结束
    page_html = page_obj.page_html()
    page_num = page_obj.num()
    return render(request, ".//user_service/user_service_list.html", {"user":range,"v":current_user,"page_html":page_html,"num":page_num})

# 添加
# def add_user_service(request):
#     if request.method=="GET":
#         service_list=models.Service.objects.all()
#         # print(service_list)
#         return render(request,".//user_service/add_user_service.html",{"service_list":service_list})
#     else:
#         # 获取用户新输入的用户名
#         username=request.POST.get("name")
#         print(username)
#         # 获取要选择的业务
#         service_id=request.POST.getlist("service")
#         print(service_id)
#         # 创建用户
#         user_obj=models.User.objects.create(username=username)
#         # 去关联用户和业务
#         user_obj.services.set(service_id)
#         return redirect("/user_service_list/")


# 编辑
@login_check
def edit_user_service(request,pk):
    if request.method=="GET":
        v = request.session.get('user')
        if v:
            user_name=models.User.objects.filter(id=pk).first()
            print(user_name)
            service_obj=models.Service.objects.all()
            return render(request,".//user_service/edit_user_service.html",{"user_name":user_name,"service_obj":service_obj,"v":v})
    else:
        user_name = models.User.objects.filter(id=pk).first()
        new_name=request.POST.get("name")
        # 获取选择的业务
        new_service=request.POST.getlist("services")
        user_name.name=new_name
        user_name.save()
        user_name.services.set(new_service)
        return redirect("/user_service_list/")




