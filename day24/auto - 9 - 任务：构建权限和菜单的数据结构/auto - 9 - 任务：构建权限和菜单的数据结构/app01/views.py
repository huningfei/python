from django.shortcuts import render

def login(request):
    """
    用户登录
    :param request:
    :return:
    """
    """
    用户登录：马帅，UserInfo表中做查询，登录成功后获取两部分数据：
    权限 = {
        "user": {"url":'/app01/user/'},
        "user_add": {"url":'/app01/user/add/'},
        "user_edit": {"url":'/app01/user/edit/(\d+)'},
        "order": {"url":'/app01/order/'},
    }
    
    菜单信息 = {
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
    
    
