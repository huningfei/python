# Create your views here.
from django.shortcuts import HttpResponse, render, redirect
from app01 import models

# 定义一些处理用户请求的函数
def index(request):
    """
    :param request: 所有跟用户请求相关的数据都封装到了一个名为request的对象中
    :return:
    """
    print(request.method)  # 拿到用户请求的方法
    print(request.path_info)  # 拿到用户请求的路径
    # 自己找文件打开然后读取内容
    # with open('index.html', "rb") as f:
    #     data = f.read()
    # return HttpResponse("o98k")
    # Django帮我打开html文件，然后把文件里面的内容读取出来给用户返回
    return render(request, "index.html")


# 登录页面
def login(request):
    # 根据用户发送请求的方法不同，做不同的操作
    print(request.method)
    if request.method == "POST":
        # 表示用户给我提交用户名和密码数据了
        # 从request中取用户 post 过来的数据
        print(request.POST)  # 是一个大字典
        # 用户名密码正确性校验
        username = request.POST.get("username", "")
        pwd = request.POST.get("password", "")
        if username == "alex" and pwd == "alexdsb":
            # 登陆成功
            # return HttpResponse("登陆成功")
            # 跳转到index页面,让用户的浏览器去访问新的页面（index页面）
            return redirect("/index/")
        else:
            # 登录失败
            return HttpResponse("登录失败")
    # 给用户返回一个页面 用来做登录
    return render(request, 'login.html')


# 出版社列表
def publisher_list(request):
    # 把业务逻辑写在这里！！！

    # 1. 查询出所有的出版社数据
    data = models.Publisher.objects.all()

    print(data)
    # 2. 在页面上中展示,将页面返回给用户
    return render(request, "publisher_list.html", {"data": data})


# 添加出版社
def add_publisher(request):
    # 当请求方法是POST的时候，表示用户填写完出版社名字 给我发数据了
    if request.method == "POST":
        # 1. 取到用户发送的数据
        publisher_name = request.POST.get("publisher_name")
        # 2. 去数据库存储
        models.Publisher.objects.create(name=publisher_name)
        # 3. 给用户返回响应， 让用户跳转到出版社列表页
        return redirect("/publisher_list/")
    return render(request, "add_publisher.html")


# 删除出版社
def delete_publisher(request):
    print(request.GET)
    # 1. 取到用户要删除的那一条数据
    delete_id = request.GET.get("id")
    # 2. 去数据库删除掉
    models.Publisher.objects.get(id=delete_id).delete()
    # 3. 删除成功之后，再跳转回出版社列表页面
    return redirect("/publisher_list/")


# 编辑出版社
def edit_publisher(request):
    # 当请求方式是POST时，表示用户已经修改完 给我发修改之后的数据了
    if request.method == "POST":
        # 取用户提交过来的数据
        edit_id = request.POST.get("id")
        new_publisher_name = request.POST.get("publisher_name")
        # 去修改数据库中指定出版社的name字段的值
        # 先根据edit_id找到要编辑的出版社
        obj = models.Publisher.objects.get(id=edit_id)
        # 修改出版社的name
        obj.name = new_publisher_name
        # 将改动同步到数据库
        obj.save()
        # 编辑成功，跳转到出版社列表页面
        return redirect("/publisher_list/")

    # 1. 获取用户要编辑的出版社的id
    edit_id = request.GET.get("id")
    # 2. 根据id去数据库找到这条记录
    obj = models.Publisher.objects.get(id=edit_id)
    # 3. 在页面上展示原来的出版社名字
    return render(request, "edit_publisher.html", {"publisher": obj})
