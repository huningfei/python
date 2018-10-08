# Create your views here.
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt  # 用djanjo自带的csrf
import json
from repository import models


@csrf_exempt
def server(request):
    # 客户端提交的最新数据
    server_dict = json.loads(request.body.decode('utf-8'))  # 把二进制转换成utf-8,
    print(server_dict)
    # 检查server表中是否有当前资产信息（根据主机名去判断）
    if not server_dict['base']['status']:  # 如果状态码有误
        return HttpResponse('获取不到信息')
    else:  # 如果状态码是正常的，就获取主机名
        hostname = server_dict['base']['data']['hostname']
        server_obj = models.Server.objects.filter(hostname=hostname).first()
        if not server_obj:  # 如果数据库里没有这个主机就创建
            # 去server表里创建信息
            tmp = {}
            tmp.update(server_dict['base']['data'])  # 基本信息
            tmp.update(server_dict['board']['data'])  # 主板信息
            server_obj = models.Server.objects.create(**tmp)  # 也是主机名

            # models.Server.objects.create(server_obj['basic']['**data'])
            # models.Server.objects.create(server_obj['board']['**data'])
            # 去创建内存
            memory_info_dict = server_dict['memory']['data']  # 获取网卡信息
            for item in memory_info_dict.values():  # 因为有多个网卡，所以需要循环
                item['server_obj'] = server_obj  # 要说明是那台服务器的
                models.Memory.objects.create(**item)
            # 去创建硬盘
            disk_info_dict = server_dict['disk']['data']
            for item in disk_info_dict.values():  # item就是key和value -slot': '0', 'pd_type': 'SAS', 'capacity': '279.396'
                item['server_obj'] = server_obj  # 就是主机名
                models.Disk.objects.create(**item)
            # 去创建网卡信息
            nic_info_dict = server_dict['nic']['data']
            for k, v in nic_info_dict.items():
                v['server_obj'] = server_obj
                v['name'] = k
                models.NIC.objects.create(**v)  # NIC表创建
            return HttpResponse('...')
        else:
            # 更新server表
            tmp = {}
            tmp.update(server_dict['base']['data'])  # 基本信息
            tmp.update(server_dict['board']['data'])  # 主板信息
            """
                'os_platform': 'linux', 
				'os_version': 'CentOS release 6.6 (Final)\nKernel \r on an \\m', 	
				'hostname': 'c1.com'
				'manufacturer': 'Parallels Software International Inc.', 
		        'model': 'Parallels Virtual Platform', 
		        'sn': 'Parallels-1A 1B CB 3B 64 66 4B 13 86 B0 86 FF 7E 2B 20 30'},
            """
            tmp.pop('hostname')
            record_list = []  # 定义一个更改列表
            for k, new_val in tmp.items():
                old_val = getattr(server_obj, k)  # 通过反射获取value
                if old_val != new_val:
                    record = "[%s]的[%s]由[%s]变更为[%s]" % (hostname, k, old_val, new_val)
                    record_list.append(record)
                    setattr(server_obj, k, new_val)  # 更新val,k代表key,表示给key赋于新的值
                    server_obj.save()
                    if record_list:
                        models.ServerRecord.objects.create(server_obj=server_obj, content=';'.join(record_list))

            # 硬盘，网卡和内存
            new_disk_info_dict = server_dict['disk']['data']  # 客户端发送过来新的数据

            """
            新的数据格式是字典
            {
            '0': {'slot': '0', 'pd_type': 'SAS', 'capacity': '279.396', 'model': 'SEAGATE ST300MM0006     LS08S0K2B5NV'}, 
            '1': {'slot': '1', 'pd_type': 'SAS', 'capacity': '279.396', 'model': 'SEAGATE ST300MM0006     LS08S0K2B5AH'}, 
            '2': {'slot': '2', 'pd_type': 'SATA', 'capacity': '476.939', 'model': 'S1SZNSAFA01085L  
             
            }
            """
            new_disk_info_list = server_obj.disk.all()
            """
            数据格式是这样的一个个对象
            [
              obj,
              obj,
            ]
            """
            new_disk_slot_set = set(new_disk_info_dict.keys())  # 拿到前面的序号
            old_disk_slot_set = {obj.slot for obj in new_disk_info_list}  # 拿到前面的序号

            add_slot_list = new_disk_slot_set.difference(old_disk_slot_set)  # 取差集
            del_slot_list = old_disk_slot_set.difference(new_disk_slot_set)
            update_slot_list = old_disk_slot_set.intersection(new_disk_slot_set)
            # 增加
            add_record_list = []
            for slot in add_slot_list:  # slot是key
                value = new_disk_info_dict[slot]  # 根据key获得value
                tmp = "添加硬盘"
                add_record_list.append(tmp)
                value['server_obj'] = server_obj
                models.Disk.objects.create(**value)
            # 删除 包含在del_slot_list里面的全部删除掉
            models.Disk.objects.filter(server_obj=server_obj, slot__in=del_slot_list).delete()

            # 更新
            record_list = []  # 定义一个更改列表
            for slot in update_slot_list:
                value = new_disk_info_dict[slot]  # slot': '0', 'pd_type': 'SAS', 'capacity': '279.396', 'model': 'SEAGATE ST300MM0006     LS08S0K2B5NV'
                obj = models.Disk.objects.filter(server_obj=server_obj, slot=slot).first()
                # print('我是更新里面的obj',obj)
                for k, new_val in value.items():
                    old_val = getattr(obj, k)
                    if old_val != new_val:
                        record = "[%s]的[%s]里面的[%s]由[%s]变更为[%s]" % (hostname,slot,k, old_val, new_val)
                        print(record)
                        record_list.append(record)
                        setattr(obj, k, new_val)
                        obj.save()

            if record_list:
                models.ServerRecord.objects.create(server_obj=server_obj, content=';'.join(record_list))


    return HttpResponse('已收到')
