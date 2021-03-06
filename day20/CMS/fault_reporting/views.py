from django.shortcuts import render, redirect, HttpResponse
from django import views
from django.contrib import auth
import random
from fault_reporting import forms
from fault_reporting import models

from django.http import JsonResponse


# Create your views here.
class LoginView(views.View):
    '''
    如果用户发送的是get就返回登录页面
    如果是post请求，先获取用户想访问那个页面用next,然后让他输入用户名密码还有验证码，先验证
    用户名和密码，然后再判断验证码是否正确，如果都是正确的，就跳转到用户访问的那个页面
    '''

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


def logout(request):
    '''
    注销用auth模块，然后跳转到登录页面
    :param request:
    :return:
    '''
    auth.logout(request)
    return redirect("/login/")


# 首页
def index(request, *args):
    '''
    index可以传参数类似 --/lob/视频/--格式的参数
    args[1]代表第二个参数，0代表第一个

    首先分别取到业务，标签，时间的个数，然后点击不同的业务，标签，或时间跳转属于自己的内容界面
    时间这里加上了try except捕获异常，因为怕用户输入的时间日期，不符合格式，如果没有这个日期则返回空

    统计数量用的是orm的聚合查询需要先导入count

    :param request:
    :param args:
    :return:
    '''
    # 取到所有的故障总结
    report_list = models.FaultReport.objects.all()
    # 如果有参数，并且参数长度是2
    if args and len(args) == 2:
        # 进入细分查询
        if args[0] == "lob":
            # 按业务线查询,
            report_list = report_list.filter(lob__title=args[1])  #args[1]指的是视频等业务
        elif args[0] == "tag":
            # 是按照标签查询
            report_list = report_list.filter(tags__title=args[1])
        else:
            # 按照日期（年月）来查询
            try:
                year, month = args[1].split("-")  #以-切割，取出年和月
                print(year)
                report_list = report_list.filter(create_time__year=year, create_time__month=month)
            except Exception:
                report_list = []
    # 导入
    from django.db.models import Count
    # 聚合查询业务线 ,title是LOB表里的title
    lob_list = models.LOB.objects.all().annotate(num=Count("faultreport")).values("title", "num")
    # 正常查询
    # lob_list = models.LOB.objects.all()
    # 取到所有标签
    # tag_list=models.Tag.objects.all()
    # 分组获取标签
    tag_list = models.Tag.objects.all().annotate(num=Count("faultreport")).values("title", "num")
    # 拿到一个日期归档数据
    archive_list = models.FaultReport.objects.all().extra(
        select={"ym": "strftime('%%Y-%%m', create_time)"}
    ).values("ym").annotate(num=Count("id")).values("ym", "num")

    return render(request, "index.html", locals())


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
        (255, 255, 140)
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
        draw_obj.text((30 * i + 30, 0), r, fill=random_color(), font=font_obj)  # text指定的是从那开始写位置，fill是字体颜色
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
    '''
    如果是get请求，就返回注册页面，用的form写的注册页面，先导入刚才写的forms模块，然后调用RggisterForm
    如果是post请求（就是提交请求），form_obj获取到用户填的所有内容，然后去校验数据格式是否正确，如果没问题，就去
    数据库里面创建数据，创建之前，要先删除re_password这个字段，因为数据库里没有这个字段
    然后接受头像文件，需要用request.FILES，去获取
    最后去数据库保存，需要把你的普通数据和头像数据分开来存储。
    注册成功之后，就跳转到登录界面，否则就报报错信息返回到页面上面
    '''

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
            # 头像文件保存到数据库,如果你的models里面写的这个字段FileField，就会自动写在服务器上面
            models.UserInfo.objects.create_user(**form_obj.cleaned_data, avatar=avatar_obj)
            res["url"] = "/login/"
        else:
            # 数据有问题
            res["code"] = 1
            res["error"] = form_obj.errors
        return JsonResponse(res)


def change_password(request):
    '''
    更改密码
    首先获取用户名，当用户要改密码的时候让他先输入旧密码，然后在输入两次新密码，当点击提交的时候，会先检查旧密码
    是否正确，如果是正确的就检查两次输入的新密码是否正确，如果两次新密码输入正确就保存，然后跳转到登录界面。如果旧密码不正确，
    就提示错误。，两次新密码不一致也提示错误

    :param request:
    :return:
    '''
    #获取用户名
    user = auth.get_user(request)
    state = None
    if request.method == 'POST':
        old_password = request.POST.get('old_password', '')
        new_password = request.POST.get('new_password', '')
        repeat_password = request.POST.get('repeat_password', '')
        if user.check_password(old_password):
            if not new_password:
                state = 'empty'
            elif new_password != repeat_password:
                state = '两次密码不一致'

                return render(request, "change_password.html", {"error_new": state, "v": user})
            else:
                user.set_password(new_password)
                user.save()
                return redirect("/login/")
        else:
            state = '原始密码不对'

            return render(request, "change_password.html", {"error_old": state, "v": user})
    return render(request, 'change_password.html', {"v": user})


