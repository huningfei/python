from django import template

from luffy_permission import settings

register = template.Library()


@register.inclusion_tag(filename="my_menu.html")
def show_menu(request):
    menu_list = request.session[settings.MENU_SESSION_KEY]
    return {"menu_list": menu_list}  # 把menu_list返回给my_menu.html这个页面
