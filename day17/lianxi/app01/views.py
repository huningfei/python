from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from django.urls import reverse
from django import views
from django.http import JsonResponse


# Create your views here.
# 出版社列表
def publisher_list(request):
    print(request.COOKIES)
    v=request.COOKIES.get("hu")
    if v=="hao":
        data = models.Publisher.objects.all()
        return render(request, "publisher_list.html", {"data": data})
    else:
        return redirect("/login/")


# 编辑出版社  url传参
# def edit_publisher(request):
#
#     if request.method=="POST":
#         #获取用户更改的id
#         edit_id=request.POST.get("id")#从浏览器传的参数获取的id
#         new_name=request.POST.get("name")#从form表单获取的名字
#         #去数据库找到这条记录
#         obj1=models.Publisher.objects.get(id=edit_id)
#         print(obj1.name)
#         obj1.name=new_name
#         obj1.save()
#         # return redirect("/publisher_list/")
#         return redirect(reverse('list'))
#     else:
#         edit_id = request.GET.get("id")
#         publisher_edit = models.Publisher.objects.get(id=edit_id)
#         return render(request,"edit_publisher.html",{"obj2":publisher_edit})

# 编辑出版社 动态传参 FBV
# def edit_publisher(request,edit_id):
#     if request.method=="POST":
#
#             new_name=request.POST.get("name")#从form表单获取的名字
#             #去数据库找到这条记录
#             obj=models.Publisher.objects.get(id=edit_id)
#             print(obj.name)
#             obj.name=new_name
#             obj.save()
#             return redirect("/publisher_list/")
#     else:
#
#         publisher = models.Publisher.objects.get(id=edit_id)
#         return render(request,"edit_publisher.html",{"obj":publisher})

# 编辑出版社 CBV动态传参
class EditPublisher(views.View):
    def get(self, request, edit_id):
        obj = models.Publisher.objects.get(id=edit_id)
        return render(request, "edit_publisher.html", {"obj": obj})

    def post(self, request, edit_id):
        obj = models.Publisher.objects.get(id=edit_id)
        new_name = request.POST.get("name")  # 获取用户输入的新名字
        obj.name = new_name
        obj.save()
        return redirect(reverse('list'))  # 跳到展示页面，用的别名


# 上传文件
class upload(views.View):
    def get(self, request):
        return render(request, "upload.html")

    def post(self, request):
        file_obj = request.FILES.get("code")
        # 保存下来
        filename = file_obj.name
        with open(filename, "wb")as f:
            for i in file_obj.chunks():
                f.write(i)
        return HttpResponse("上传成功")


# json格式化
class JsonTest(views.View):
    def get(self, request):
        res = {"code": 0, "data": "alex"}
        res2 = ["alex", "污Sir", "金老板", "小姨妈", "MJJ"]
        return JsonResponse(res2, safe=False)


# 模板语法
def template_test(request):
    data = ["金老板", "景女神", "MJJ"]
    # data=""
    filesize = 12345
    import datetime
    today = datetime.datetime.today()
    value = "<a href='#'>点我</a>"

    class Person(object):
        def __init__(self, name, dream):
            self.name = name
            # self.dream=dream

        def dream(self):
            return "我的梦想是学好python"

    pw = Person("bob", "环游世界")
    return render(request, "template_test.html", {
        "data": data,
        "file_size": filesize,
        "today": today,
        "value": value,
        "person": pw

    })


# csrf 跨站请求
def csrf_test(request):
    if request.method == "POST":
        print(request.POST)
        return HttpResponse("OK")
    else:
        return render(request, "csrf_test.html")


# book_list
def book_list(request):
    # 去数据库查询所有的书籍
    data = models.Book.objects.all()
    return render(request, "book_list.html", {"book_list": data})


# add_book
def add_list(request):
    if request.method == "POST":
        name = request.POST.get("title")
        # print(name)
        publisher_id = request.POST.get("publisher")
        publisher_obj = models.Book.objects.get(id=publisher_id)

        models.Book.objects.create(title=name, publisher_id=publisher_id)
        return redirect("/book_list/")
    else:
        data = models.Publisher.objects.all()
        return render(request, "add_book.html", {"publisher_list": data})


# del_book
def del_book(request, pk):
    if request.method == "GET":
        models.Book.objects.get(id=pk).delete()
        return redirect("/book_list")

# edit_book
def edit_book(request,pk):
    if request.method=="GET":
        book_id=models.Book.objects.get(id=pk)
        publisher_obj=models.Publisher.objects.all()
        return render(request,"edit_book.html",{"book":book_id,"publisher_list":publisher_obj})
    else:
        book_obj= models.Book.objects.get(id=pk)# 更改之前的书名字
        new_title=request.POST.get("title")
        new_publisher_id=request.POST.get("publisher")
        book_obj.title=new_title
        book_obj.publisher_id=new_publisher_id
        book_obj.save()
        return redirect("/book_list/")



def login(request):
    if request.method=="POST":
        next = request.POST.get("next")
        print(next)
        username=request.POST.get("username")
        pwd=request.POST.get("pwd")
        if username=="alex" and pwd=="123":
            if next:
                rep = redirect(next)
            else:
                rep=redirect("/publisher_list/")
            rep.set_signed_cookie("hu", "hao", salt="ooxx", max_age=7)
            return rep
        else:
            return HttpResponse("用户名或者密码错误")
    else:
        return render(request,"login.html")

