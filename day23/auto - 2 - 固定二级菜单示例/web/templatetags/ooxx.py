from django.template import Library
from django.conf import settings
import copy
import re
register = Library()


# 定义一个函数
# @register.simple_tag()
# def show_menu(a):
#     return '999'


@register.inclusion_tag('menu.html')
def get_menu(request):
    '''
    获取菜单
    :param request:
    :return:
    '''
    new_menu_list = copy.deepcopy(settings.MENU_LIST)
    flag = False
    for item in new_menu_list: # item就是menu_list里面的一级菜单
        for child in item['children']:  # 循环children里面的菜单 [个人中心，添加用户，....]
            reg="^{0}$".format(child['url']) # ^/web/user/1/$
            if re.match(reg,request.path_info): #如果请求的菜单和正则匹配
                if child['is_menu']: # 如果是true
                    child['class'] = 'active'  # 子类class ，如果匹配上就让目录的class=active
                else:
                    index=child['parent_index'] # 关联菜单，找出要选中菜单的索引
                    item['children'][index]['class']='active'  # 找到这个菜单的索引，然后选中及加上active
                item['class'] = ''  # 父 类class  就是hide
                flag = True
                break
        if flag:
            break

    return {'menu_list': new_menu_list}  # 把new_menu_list传给menu里面的代码
