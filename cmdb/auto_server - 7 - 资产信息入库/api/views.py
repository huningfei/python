import json
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from api import models
from api import service

"""
@method_decorator(csrf_exempt,name='dispatch')
class AssetView(View):
    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    def get(self,requset,*args,**kwargs):
        host_list = ['c1.com', 'c2.com', 'c3.com']
        return HttpResponse(json.dumps(host_list))

    def post(self,request,*args,**kwargs):
        info = json.loads(request.body.decode('utf-8'))
        print(info)
        return HttpResponse('收到了')
"""

from rest_framework.views import APIView
from rest_framework.response import Response


class AssetView(APIView):
    def get(self, requset, *args, **kwargs):
        host_list = ['c1.com', 'c2.com', 'c3.com']
        # return HttpResponse(json.dumps(host_list))
        return Response(host_list)

    def post(self, request, *args, **kwargs):
        """
        资产汇报的API
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        print(request.data)
        # ###################### agent模式汇报 ######################
        result = {'status':True,'data':None,'error':None}
        asset_type = request.data.get('type')
        if asset_type == 'create':
            # ################## 增加资产 ##################

            # 1. 在server表添加数据
            server_dict = {}
            server_dict.update(request.data['basic']['data'])
            server_dict.update(request.data['cpu']['data'])
            server_dict.update(request.data['board']['data'])
            # 新建服务器，server代表新创建的数据
            server = models.Server.objects.create(**server_dict)

            # 2. 硬盘
            disk_info = request.data['disk']['data']
            for k,v in disk_info.items():
                v['server'] = server
                models.Disk.objects.create(**v)
            # 3. 网卡
            nic_info = request.data['nic']['data']
            for k,v in nic_info.items():
                print(k,v)
                v['server'] = server
                v['name'] = k
                models.NIC.objects.create(**v)
            # 4. 内存
            memory_info = request.data['memory']['data']
            for k,v in memory_info.items():
                v['server'] = server
                models.Memory.objects.create(**v)
        elif asset_type == 'update':
            # 更新资产
            hostname = request.data['basic']['data']['hostname']
            server = models.Server.objects.get(hostname=hostname)
            service.process_basic(request,hostname)
            service.process_disk(request,server)
            service.process_nic(request, server)
            service.process_memory(request, server)


        elif asset_type == 'host_update':
            # 更新资产+更新主机名
            # 获取主机名
            hostname = request.data['cert'] # 老的主机名
            server = models.Server.objects.filter(hostname=hostname)
            service.process_basic(request, hostname)
            service.process_disk(request, server)
            service.process_nic(request, server)
            service.process_memory(request, server)


        result['data'] = request.data['basic']['data']['hostname']
        print(result['data'])
        return Response(result)

