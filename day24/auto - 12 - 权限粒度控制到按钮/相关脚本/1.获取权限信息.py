permission_menu_list = [
    {
        'permissions__title': '用户列表',
        'permissions__url': '/app01/user/',
        'permissions__name': 'user_list',
        'permissions__menu_id': 1,
        'permissions__menu__title': '用户管理',
        'permissions__menu__icon': 'fa-clipboard',
        'permissions__parent_id': None,
        'permissions__parent__name': None
    },
    {
        'permissions__title': '添加用户',
        'permissions__url': '/app01/user/add/',
        'permissions__name': 'user_add',
        'permissions__menu_id': None,
        'permissions__menu__title': None,
        'permissions__menu__icon': None,
        'permissions__parent_id': 1,
        'permissions__parent__name': 'user_list'
    },
    {
        'permissions__title': '编辑用户',
        'permissions__url': '/app01/user/edit/(\\d+)',
        'permissions__name': 'user_edit',
        'permissions__menu_id': None,
        'permissions__menu__title': None,
        'permissions__menu__icon': None,
        'permissions__parent_id': 1,
        'permissions__parent__name': 'user_list'
    },
    {
        'permissions__title': '订单列表',
        'permissions__url': '/app01/order/',
        'permissions__name': 'order',
        'permissions__menu_id': 2,
        'permissions__menu__title': '商品管理',
        'permissions__menu__icon': 'fa-clipboard',
        'permissions__parent_id': None,
        'permissions__parent__name': None
    }
]

"""
permission_dict = {
    "user_list": {"url":'/app01/user/'},
    "user_add": {"url":'/app01/user/add/'},
    "user_edit": {"url":'/app01/user/edit/(\d+)'},
    "order": {"url":'/app01/order/'},
}
"""

permission_dict = {}
for item in permission_menu_list:
    name = item['permissions__name']
    url = item['permissions__url']
    menu_id = item['permissions__menu_id']
    parent_name = item['permissions__parent__name']
    permission_dict[name] = {'url': url,'menu_id':menu_id,'parent_name':parent_name}
    
print(permission_dict)
