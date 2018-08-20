from django.shortcuts import render, redirect, HttpResponse
from functools import wraps
from app01 import models
import mypage


# Create your views here.
def login_check(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        next = request.path_info
        # 登录验证
        # 取Session
        v = request.session.get("s21")
        if v == "hao":
            return func(request, *args, **kwargs)
        else:
            return redirect("/login/?next={}".format(next))

    return inner


# 登录 session验证
def login(request):
    if request.method == "POST":
        next = request.GET.get("next")
        username = request.POST.get("username")
        pwd = request.POST.get("pwd")
        if username == "alex" and pwd == "123":
            if next:
                rep = redirect(next)
            else:
                rep = redirect("/secode/")
            request.session["s21"] = "hao"
            request.session.set_expiry(70)
            return rep
        else:
            return HttpResponse("走吧")
    else:
        return render(request, "login.html")


@login_check
def index(request):
    return render(request, "index.html")


@login_check
def secode(request):
    return render(request, "secode.html")

# 分页
def book_list(request):
    book=models.Book.objects.all()
    total_count=book.count()
    current_page=request.GET.get("page")
    #分页功能开始
    page_boj = mypage.MyPage(current_page, total_count, url_prefix="book_list")
    data = book[page_boj.start:page_boj.end]  # 从第几页显示到第几页
    page_html = page_boj.page_html()  # 页面
    page_num = page_boj.num()  # 序号
    return render(request,"book_list.html",{"book":data,"page_html":page_html,"num":page_num})

    # # 查找所有书籍
    # books = models.Book.objects.all()
    # # 拿到总数据量
    # total_count = books.count()
    # # 每一页显示多少条数据
    # per_page = 10
    # # 页面最多显示多少页码
    # max_show = 7
    # # 最多显示页码数的一半
    # half_show = max_show // 2  # 地板除，没有余数
    # # 从url拿到page参数
    # current_page = request.GET.get("page")
    # try:
    #     current_page = int(current_page)
    # except Exception as e:
    #     # 如果输入的页面有误默认显示第一页
    #     current_page = 1
    # # 求总共需要多少页显示,总数据除以每页显示多少条
    # total_page, more = divmod(total_count, per_page)
    # if more:  # 代表有余数
    #     total_page += 1  # 需要在增加一个页码，才可以显示
    # # 如果输入的当前页码大于总数据的页码
    # if current_page > total_page:
    #     current_page = total_page
    # # 计算一下，显示页码的起点和终点分别是多少
    # show_page_start = current_page - half_show
    # show_page_end = current_page + half_show
    # # 当前页码 - half_show <=0
    # if current_page - half_show <= 0:
    #     show_page_start = 1
    #     show_page_end = max_show
    # # 当前页码数 + half_show >= total-page
    # if current_page + half_show >= total_page:
    #     show_page_end = total_page
    #     show_page_start = total_page - max_show
    # # 实际的总页码数 < max_show  比如我一共2页
    # if total_page < max_show:
    #     show_page_start = 1
    #     show_page_end = total_page
    #
    # # 数据切片的起点
    # data_start = (current_page - 1) * per_page
    # # 数据切片的终点
    # data_end = current_page * per_page
    # data = books[data_start:data_end]
    #
    # tmp = []
    # page_html_start = '<nav aria-label="Page navigation" class="text-center"><ul class="pagination">'
    # page_html_end = '</ul></nav>'
    # tmp.append(page_html_start)
    # # 添加一个首页
    # tmp.append('<li><a href="/book_list?page=1">首页</a></li>')
    #
    # # 添加一个上一页
    # # 当当前页是第一页的时候不能再点击上一页
    # if current_page - 1 <= 0:
    #     tmp.append(
    #         '<li class="disabled"><a href="#" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>')
    # else:
    #     tmp.append(
    #         '<li><a href="/book_list?page={}" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'.format(
    #             current_page - 1))
    # # for循环添加要展示的页码
    # for i in range(show_page_start, show_page_end + 1):
    #     # 如果for循环的页码等于当前页码，给li标签加一个active的样式
    #     if current_page == i:
    #         tmp.append('<li class="active"><a href="/book_list?page={0}">{0}</a></li>'.format(i))
    #     else:
    #         tmp.append('<li><a href="/book_list?page={0}">{0}</a></li>'.format(i))
    # # 添加一个下一页
    # # 当前 当前页已经是最后一页，应该不让下一页按钮能点击
    # if current_page + 1 > total_page:
    #     tmp.append(
    #         '<li class="disabled"><a href="#" aria-label="Previous"><span aria-hidden="true">&raquo;</span></a></li>')
    # else:
    #     tmp.append(
    #         '<li><a href="/book_list?page={}" aria-label="Previous"><span aria-hidden="true">&raquo;</span></a></li>'.format(
    #             current_page + 1))
    # # 添加一个尾页
    # tmp.append('<li><a href="/book_list?page={}">尾页</a></li>'.format(total_page))
    # tmp.append(page_html_end)
    #
    # page_html = "".join(tmp)
    #
    # # 序号
    # xuhao=(current_page-1)*per_page
    #
    # return render(request, "book_list.html", {"books": data, "page_html": page_html,"num":xuhao})

# 分页
def publisher_list(request):
    publisher = models.Publisher.objects.all()
    total_count = publisher.count()  # 总页面
    current_page = request.GET.get("page")

    page_boj = mypage.MyPage(current_page, total_count, url_prefix="publisher_list") #调用Mypage这个类，并传三个参数
    data = publisher[page_boj.start:page_boj.end] # 从第几页显示到第几页
    page_html = page_boj.page_html() # 页面
    page_num=page_boj.num() # 序号
    return render(request, "publisher_list.html", {"publisher": data, "page_html": page_html,"num":page_num})

def test(request):
    '''
    views里面的视图函数
    :param request:
    :return:
    '''
    print("这是test视图函数")
    # print(request.s21)
    print(id(request))
    return HttpResponse("o98k")