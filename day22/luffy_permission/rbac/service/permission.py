from django.conf import settings


def init_permission(request, user_obj):
    '''
在session中初始化权限信息和菜单信息的函数
    :param request: 请求对象
    :param user_obj:当前登录用户
    :return:
    '''

    # user_obj.roles.all()那到当前用户的所有角色
    ret = user_obj.roles.all().values("permissions__url",
                                      "permissions__icon",
                                      "permissions__is_menu",
                                      "permissions__title"
                                      ).distinct()  # 取到去重之后的权限
    # 定义一个权限列表
    permission_list = []
    # 定义一个专门用来存放当前用户菜单的列表
    menu_list = []
    for item in ret:
        print(item)  # item是个大列表
        permission_list.append({"permissions__url": item["permissions__url"]})  # 添加到权限列表
        if item["permissions__is_menu"]:  # 如果为真
            menu_list.append({
                "title": item["permissions__title"],
                "icon": item["permissions__icon"],
                "url": item["permissions__url"]
            })

    # 将用户权限列表信息，存到session中
    request.session[settings.PERMISSION_SESSION_KEY] = permission_list
    # 把当前用户的所有菜单存放到sessioin
    request.session[settings.MENU_SESSION_KEY] = menu_list
