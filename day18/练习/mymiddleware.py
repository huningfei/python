'''
自己定义的中间件
'''
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,render


# class MD1(MiddlewareMixin):
#     def process_request(self, request):
#         print("这是md1中的process_request方法")
#         print(id(request))
#         request.s21 = "好"
#         # return HttpResponse("呵呵1")
#         # return render(request,"weihu.html")
#
#     def process_response(self,request,response):
#         print("这是md1中的process_response方法")
#         return response
#     def process_view(self,request,view_func,view_args,view_kwargs):
#         print("=" * 120)
#         # print(view_func.__name__)  # 查看名字
#         # print(view_func.__doc__) # 查看文本注释
#         # view_func(request)
#         # print("-" * 120)
#         print("这是md1中的process_view方法")
#         # return HttpResponse("啦啦")
#
#     def process_template_response(self, request, response):
#
#
#         print("这是MD1中的process_template_response方法！")
#         return response
#
#
#
# class MD2(MiddlewareMixin):
#     def process_request(self, request):
#         print("这是md2中的process_request方法")
#         print(id(request))
#         request.s21 = "好"
#         # return HttpResponse("呵呵2")
#
#     def process_response(self, request, response):
#         print("这是md2中的process_response方法")
#         return response
#         # return  HttpResponse("MD2-ressponse")
#
#     def process_view(self,request,view_func,view_args,view_kwargs):
#         print("=" * 120)
#         # print(view_func.__name__)
#         # print(view_func.__doc__)
#         # view_func(request)
#         # print("-" * 120)
#         print("这是md2中的process_view方法")
#         # return HttpResponse("啦啦")
#
#     def process_template_response(self, request, response):
#         print("这是MD2中的process_template_response方法！")
#         return response

import time
D={}
class Xianzhi(MiddlewareMixin):
    def process_request(self,request):
        ip=request.META.get("PEMOTE_ADDR")
        now=time.time()
        if ip not in D:
            D[ip]=[]
            # print(D)
        history=D[ip]
        print(history)
        while history and now-history[-1] >10: # 当现在的访问时间跟最早的访问时间相差大于10秒的时候，则删除最早的访问时间
            history.pop()
        if len(history)>=3:
            return HttpResponse("你在10秒之内访问次数已经超过三次")
        else:
            history.insert(0,now)
