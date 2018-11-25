# Create your views here.
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt  # 用djanjo自带的csrf
import json
from .plugins import PluginManger
from datetime import date
from repository import models
from django.db.models import Q


@csrf_exempt  #  这个函数不走csrf_token
def server(request):
    if request.method == "GET":
        current_date = date.today()
        # 获取今日未采集的主机列表
        # 条件是更新时间为空，并且更新的时间小于现在的时间，还有主机的状态是在线状态才会拿到未采集的列表 ，双下划线date就是只取年月日
        host_list = models.Server.objects.filter(
            Q(Q(latest_date=None) | Q(latest_date__date__lt=current_date)) & Q(server_status_id=2)
        ).values('hostname')
        host_list = list(host_list)
        print(host_list)
        return HttpResponse(json.dumps(host_list))
    elif request.method == "POST":

        # 客户端提交的最新数据
        server_dict = json.loads(request.body.decode('utf-8'))  # 把二进制转换成utf-8,
        print(server_dict)
        # 检查server表中是否有当前资产信息（根据主机名去判断）
        if not server_dict['basic']['status']:  # 如果状态码有误
            return HttpResponse('获取不到信息')

        manager = PluginManger()
        response = manager.exec(server_dict)
        return HttpResponse(json.dumps(response))
    # hostname = server_dict['basic']['data']['hostname']
    # server_obj = models.Server.objects.filter(hostname=hostname).first()
    # if not server_obj:
    #     # 创建服务器，创建硬盘内存网卡
    #     tmp = {}
    #     tmp.update(server_dict['basic']['data'])
    #     tmp.update(server_dict['board']['data'])
    #     server_obj = models.Server.objects.create(**tmp)
    #     # 网卡，内存，硬盘
    #
    #     # 硬盘
    #     disk_info_dict = server_dict['disk']['data']
    #     for item in disk_info_dict.values():
    #         item['server_obj'] = server_obj
    #         models.Disk.objects.create(**item)
    #     # 内存
    #     mem_info_dict = server_dict['memory']['data']
    #     for item in mem_info_dict.values():
    #         item['server_obj'] = server_obj
    #         models.Memory.objects.create(**item)
    #     # 网卡
    #     nic_info_dict = server_dict['nic']['data']
    #     for k, v in nic_info_dict.items():
    #         v['server_obj'] = server_obj
    #         v['name'] = k
    #         models.NIC.objects.create(**v)
    #
    # else:  # 更新
    #     # 更新server表
    #     tmp = {}
    #     tmp.update(server_dict['basic']['data'])
    #     tmp.update(server_dict['board']['data'])
    #     tmp.pop('hostname')
    #     record_list = []
    #     for k, new_val in tmp.items():
    #         old_val = getattr(server_obj, k)
    #         if old_val != new_val:
    #             record = "[%s]的[%s]由[%s]变更为[%s]" % (server_obj.hostname, k, old_val, new_val)
    #             record_list.append(record)
    #             setattr(server_obj, k, new_val)
    #     server_obj.save()
    #     if record_list:
    #         models.ServerRecord.objects.create(server_obj=server_obj, content=';'.join(record_list))
    #
    #     # 硬盘
    #     new_disk_info_dict = server_dict['disk']['data']  # 客户端发送过来新的数据
    #
    #
    #     """
    #     新的数据格式是字典
    #     {
    #     '0': {'slot': '0', 'pd_type': 'SAS', 'capacity': '279.396', 'model': 'SEAGATE ST300MM0006     LS08S0K2B5NV'},
    #     '1': {'slot': '1', 'pd_type': 'SAS', 'capacity': '279.396', 'model': 'SEAGATE ST300MM0006     LS08S0K2B5AH'},
    #     '2': {'slot': '2', 'pd_type': 'SATA', 'capacity': '476.939', 'model': 'S1SZNSAFA01085L
    #
    #     }
    #     """
    #     new_disk_info_list = server_obj.disk.all()
    #     """
    #     数据格式是这样的一个个对象
    #     [
    #       obj,
    #       obj,
    #     ]
    #     """
    #     new_disk_slot_set = set(new_disk_info_dict.keys())  # 拿到前面的序号 {'3', '4', '5', '11', '9', '1', '2'}
    #     old_disk_slot_set = {obj.slot for obj in new_disk_info_list}  # 拿到前面的序号
    #
    #     add_slot_list = new_disk_slot_set.difference(old_disk_slot_set)  # 取差集
    #     del_slot_list = old_disk_slot_set.difference(new_disk_slot_set)
    #     update_slot_list = old_disk_slot_set.intersection(new_disk_slot_set)
    #
    #     # 增加
    #     add_record_list = []
    #     for slot in add_slot_list:  # slot是key
    #         value = new_disk_info_dict[slot]  # 根据key获得value
    #         tmp = "添加硬盘"
    #         add_record_list.append(tmp)
    #         value['server_obj'] = server_obj
    #         models.Disk.objects.create(**value)
    #     # 删除 包含在del_slot_list里面的全部删除掉
    #     models.Disk.objects.filter(server_obj=server_obj, slot__in=del_slot_list).delete()
    #
    #     # 更新
    #     # record_list = []  # 定义一个更改列表
    #     for slot in update_slot_list:
    #         # print(slot) # slot是序号，0,2,3
    #         value = new_disk_info_dict[slot]  # slot': '0', 'pd_type': 'SAS', 'capacity': '279.396', 'model': 'SEAGATE ST300MM0006     LS08S0K2B5NV'
    #         obj = models.Disk.objects.filter(server_obj=server_obj, slot=slot).first()
    #         # print('我是更新里面的obj',obj)
    #         for k, new_val in value.items():
    #             old_val = getattr(obj, k)
    #             # print(old_val)
    #
    #             if old_val != new_val:
    #                 # record = "[%s]的[%s]里面的[%s]由[%s]变更为[%s]" % (self.server_obj.hostname, slot, k, old_val, new_val)
    #                 # print(record)
    #                 # record_list.append(record)
    #                 # print(record_list)
    #                 setattr(obj, k, new_val)
    #         obj.save()
    # return HttpResponse('OK')


