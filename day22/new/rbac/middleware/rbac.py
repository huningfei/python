'''
自定义rbac中间件
'''
from django.utils.deprecation import  MiddlewareMixin
from django.shortcuts import redirect,HttpResponse,render
import re
from django.conf import settings

class RBACMiddleware(MiddlewareMixin):
    def process_request(self,request):
        '''
        自定义权限校验的中间件
        :param request: 请求对象
        :return:
        '''
        # 1 取到当前这次请求访问的url是什么
        url=request.path_info   # request.get_full_path()
        # 过滤白名单
        for item in settings.PERMISSION_WHITE_URL:
            reg="^{}$".format(item)
            if re.match(reg,url):
                return None
        # 取到当前用户的权限列表
        permission_list=request.session.get(settings.PERMISSION_SESSION_KEY,None)
        # 进行权限校验
        if  permission_list is None:
            # 用户没登录
            return redirect("/login/")
        for i in permission_list:
            reg="^{}$".format(i['permissions__url'])
            if re.match(reg,url):
                break
        else:
            return HttpResponse("你没有此权限")
