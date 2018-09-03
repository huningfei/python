from django.shortcuts import render, redirect, HttpResponse
from django import views
from django.contrib import auth
import random
from fault_reporting import forms
from fault_reporting import models

from django.http import JsonResponse


# Create your views here.
class LoginView(views.View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        next_url = request.GET.get("next", "/index/")
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        v_code = request.POST.get("vcode", "").upper()  # 如果用户不写验证码就是空
        if v_code == request.session.get("v_code"):

            user_obj = auth.authenticate(username=username, password=pwd)
            if user_obj:
                auth.login(request, user_obj)  # auth认证登录
                return redirect(next_url)
            else:
                return render(request, "login.html", {"error_msg": "用户名或密码错误"})
        else:
            return render(request, "login.html", {"error_msg": "验证码错误"})


# 首页
def index(request):
    return render(request, "index.html")


# 验证码路径
def vcode(request):
    from PIL import Image, ImageDraw, ImageFont  # 导入绘图模块
    # 定义一个生成随机颜色代码的函数
    def random_color():
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    # 创建一个随机背景颜色的图片对象
    image_obj = Image.new(
        "RGB",
        (250, 35),  # 背景图片的长和宽
        random_color()
    )
    # 在该图片对象上生成一个画笔对象
    draw_obj = ImageDraw.Draw(image_obj)
    # 加载一个字体对象
    font_obj = ImageFont.truetype('static/font/kumo.ttf', 28)  # 字体大小
    tmp = []
    for i in range(5):
        l = chr(random.randint(97, 122))  # 生成随机的小写字母
        u = chr(random.randint(65, 90))  # 生成随机的大写字母
        n = str(random.randint(0, 9))  # 生成一个随机的数字
        # 从上面三个随机选一个
        r = random.choice([l, u, n])
        # 将选中过的那个字符写到图片上
        draw_obj.text((40 * i + 30, 0), r, fill=random_color(), font=font_obj)  # text指定的是从那开始写位置，fill是字体颜色
        tmp.append(r)

        v_code = "".join(tmp).upper()
        # 将生成的验证码保存
        request.session["v_code"] = v_code

        # 直接在内存中保存图片替代io操作
    from io import BytesIO
    f1 = BytesIO()
    image_obj.save(f1, format="PNG")  # 将背景图片保存到f1里面
    img_data = f1.getvalue()  # 去f1取图片
    return HttpResponse(img_data, content_type="image/png")


# 注册
class RegisterView(views.View):
    def get(self, request):
        form_obj = forms.RegisterForm()
        return render(request, "register.html", locals())

    def post(self, request):
        res = {"code": 0}
        form_obj = forms.RegisterForm(request.POST)
        if form_obj.is_valid():
            # 数据没问题，去数据库创建记录
            form_obj.cleaned_data.pop("re_password")
            # 头像数据，文件对象
            avatar_obj = request.FILES.get("avatar")
            # 头像文件保存到数据库
            models.UserInfo.objects.create_user(**form_obj.cleaned_data, avatar=avatar_obj)
            res["url"] = "/login/"
        else:
            # 数据有问题
            res["code"] = 1
            res["error"] = form_obj.errors
        return JsonResponse(res)


#ajax_upload
def ajax_upload(requst):
    return render(requst,"ajax_upload.html")

#upload
def upload(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        # 从上传的文件数据中拿到 avatar对应的文件对象
        file_obj = request.FILES.get("avatar")
        # 在服务端新建一个和上传文件同名的新文件
        with open(file_obj.name, "wb") as f:
            # 从上传文件对象中一点一点读数据
            for i in file_obj:
                # 写入服务端新建的文件
                f.write(i)
        return HttpResponse("OK")
    return render(request, "upload.html")