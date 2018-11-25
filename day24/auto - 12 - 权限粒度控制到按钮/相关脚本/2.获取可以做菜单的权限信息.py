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


permission_list = []

for item in permission_menu_list:
    menu_id = item['permissions__menu_id']
    if menu_id:
        permission_list.append(item)
    
print(permission_list)

"""
[
    {'permissions__title': '用户列表', 'permissions__url': '/app01/user/', 'permissions__name': 'user_list', 'permissions__menu_id': 1, 'permissions__menu__title': '用户管理', 'permissions__menu__icon': 'fa-clipboard', 'permissions__parent_id': None, 'permissions__parent__name': None},
    {'permissions__title': '订单列表', 'permissions__url': '/app01/order/', 'permissions__name': 'order', 'permissions__menu_id': 2, 'permissions__menu__title': '商品管理', 'permissions__menu__icon': 'fa-clipboard', 'permissions__parent_id': None, 'permissions__parent__name': None}
]

"""