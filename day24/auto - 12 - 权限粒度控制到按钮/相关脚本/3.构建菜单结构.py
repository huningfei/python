permission_list = [
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
		'permissions__title': '订单列表',
		'permissions__url': '/app01/order/',
		'permissions__name': 'order',
		'permissions__menu_id': 2,
		'permissions__menu__title': '商品管理',
		'permissions__menu__icon': 'fa-clipboard',
		'permissions__parent_id': None,
		'permissions__parent__name': None
	},
]
"""
menu_dict = {
	1:{
		'title':'用户管理',
		'icon':'fa-clipboard',
		'children':[
			{'title':'用户列表','url':'/app01/user/'},
		]
	},
	2:{
		'title':'商品管理',
		'icon':'fa-clipboard',
		'children':[
			{'title':'订单列表','url':'/app01/order/'},
			
		]
	}
	
}
"""
menu_dict = {}

for item in permission_list:
    menu_id = item['permissions__menu_id']
    if menu_id in menu_dict:
        menu_dict[menu_id]['children'].append({'title':item['permissions__title'],'url':item['permissions__url'],'name':item['permissions__name'] })
    else:
        menu_dict[menu_id] = {
            'title': item['permissions__menu__title'],
            'icon': item['permissions__menu__icon'],
            'children':[
                {'title':item['permissions__title'],'url':item['permissions__url'],'name':item['permissions__name'] }
            ]
        }
        
print(menu_dict)


