import datetime
from django import template

register = template.Library()
# 把我写的函数注册成一个自定义的filter函数，就能在模板语言里使用了
@register.filter()
def alex(arg, delta="7"):
    try:
        delta = int(delta)
    except Exception:
        delta = 7
        # 在原来时间基础上加7天
    ret = arg + datetime.timedelta(days=delta)
    # 把时间对象格式化成字符串格式
    return ret.strftime("%Y-%m-%d %H:%M:%S")


# 把一个函数注册成自定义的simple_tag
@register.simple_tag()
def gold(arg1, arg2, arg3):
    return "{}-{}-{}".format(arg1, arg2, arg3)


# 用一些数据去填充一段HTML代码 把HTML代码返回给调用方
# 类似于一个简化版的render(request, "xx.html", {})函数
@register.inclusion_tag(filename="ul.html")
def show_menu(arg): #必须传一个参数
    ret = [i for i in range(arg)] #返回一个可迭代的对象
    return {"num": ret}