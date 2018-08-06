from django.shortcuts import render, HttpResponse, redirect
from app01 import models


def index(request):
    '''

    :param request: 所有的用户请求都封装到了一个名为request函数中
    :return:
    '''
    print(request.method)  # 拿到用户的请求的方法
    print(request.path_info)  # 拿到用户的请求路径
    return render(request, "index.html")


def home(request):
    return render(request, "home.html")


# 登录页面
def login(request):
    if request.method == "POST":
        # print(request.POST)
        user = request.POST.get("username", "")  # 这里的username必须和html里面的name的值一致
        pwd = request.POST.get("password", "")
        # print(username, pwd)
        try:
            obj = models.User.objects.get(username=user)
        except Exception:
            return HttpResponse("登录失败")
        if obj.username == user and obj.password == pwd:
            return redirect("/index/")
        else:
            return HttpResponse("登录失败")
    else:
        return render(request, 'login.html')


# Create your views here.
# 展示页面
def publisher_list(request):
    data = models.Publisher.objects.all()
    # print(data)
    return render(request, "publisher_list.html", {"data": data})


# 添加出版社
def add_publisher(request):
    if request.method == "POST":

        # 获取用户添加的出版社名字
        publisher_name = request.POST.get("publisher_name")  # 从add页面中获取名字

        # 写入到数据库中
        models.Publisher.objects.create(name=publisher_name)
        # 添加成功之后，给用户返回一个网页

        return redirect("/publisher_list/")
    else:  # 如果是get则给用户返回一个添加页面
        return render(request, "add_publisher.html")

    #删除出版社
def del_publisher(request):
    print(request.GET)

    # 获取用户删除的id
    data_id=request.GET.get("id")
    #去数据库里面删除
    models.Publisher.objects.get(id=data_id).delete()
    return redirect("/publisher_list/")
#编辑出版社
def edit_publisher(request):
    if request.method == "POST":
        #获取用户要更改的数据
        edit_id=request.POST.get("id")
        new_publish_name=request.POST.get("publisher_name")
        #去修改数据库中指定出版社的name字段
        #根据edit_id去找到要更改的出版社
        obj=models.Publisher.objects.get(id=edit_id)
        print(obj)
        #修改出版社名字
        obj.name=new_publish_name
        #同步到数据库
        obj.save()
        return redirect("/publisher_list/")
    else:#如果是get就执行下面的
        # 1. 获取用户要编辑的出版社的id
        edit_id = request.GET.get("id")
        # 2. 根据id去数据库找到这条记录
        obj = models.Publisher.objects.get(id=edit_id)
        # 3. 在页面上展示原来的出版社名字
        return render(request, "edit_publisher.html", {"publisher": obj})

