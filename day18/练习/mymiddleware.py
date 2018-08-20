'''
自己定义的中间件
'''
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,render


class MD1(MiddlewareMixin):
    def process_request(self, request):
        print("这是md1中的process_request方法")
        print(id(request))
        request.s21 = "好"
        # return HttpResponse("呵呵1")
        # return render(request,"weihu.html")

    def process_response(self,request,response):
        print("这是md1中的process_response方法")
        return response


class MD2(MiddlewareMixin):
    def process_request(self, request):
        print("这是md2中的process_request方法")
        print(id(request))
        request.s21 = "好"
        return HttpResponse("呵呵2")

    def process_response(self, request, response):
        print("这是md2中的process_response方法")
        # return response
        return  HttpResponse("MD2-ressponse")