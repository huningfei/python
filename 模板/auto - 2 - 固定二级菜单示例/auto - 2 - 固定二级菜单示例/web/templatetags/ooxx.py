from django.template import Library
from django.conf import settings
import copy

register = Library()


# 定义一个函数
# @register.simple_tag()
# def show_menu(a):
#     return '999'


@register.inclusion_tag('menu.html')
def get_menu(request):
    new_menu_list = copy.deepcopy(settings.MENU_LIST)
    flag = False
    for item in new_menu_list:
        for child in item['children']:
            if request.path_info == child['url']:
                child['class'] = 'active'  # 子类class
                item['class'] = ''  # 父 类class
                flag = True
                break
        if flag:
            break

    return {'menu_list':new_menu_list}
