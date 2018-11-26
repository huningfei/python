#!/usr/bin/python
# -*- coding:utf-8 -*-
from api import models

def process_basic(request,hostname):
    basic_dict = {}
    basic_dict.update(request.data['basic']['data'])
    basic_dict.update(request.data['cpu']['data'])
    basic_dict.update(request.data['board']['data'])
    models.Server.objects.filter(hostname=hostname).update(**basic_dict)


def process_disk(request,server):
    # 1.1 获取数据库中的硬盘信息
    disk_queryset = models.Disk.objects.filter(server=server)

    # 1.2 最新汇报来的硬盘信息
    disk_info = request.data['disk']['data']

    disk_queryset_set = {row.slot for row in disk_queryset}
    disk_info_set = set(disk_info)

    update_disk_slot_list = disk_info_set & disk_queryset_set
    add_disk_slot_list = disk_info_set - disk_queryset_set
    del_disk_slot_list = disk_queryset_set - disk_info_set

    # 更新
    for slot in update_disk_slot_list:
        # models.Disk.objects.filter(slot=slot, server=server).update(**disk_info[slot])
        obj = models.Disk.objects.filter(slot=slot, server=server).first()  # 找出对应的服务器上面对应的序号
        row_dict = disk_info[slot]  # 代表客户端发送过来的硬盘数据
        record_list = []
        for name, new_value in row_dict.items():
            old_value = str(getattr(obj, name)) #都是字符串互相比较
            if old_value != new_value:
                setattr(obj, name, new_value)
                verbose_name = models.Disk._meta.get_field(name).verbose_name
                msg = "【硬盘变更】槽位%s：%s由%s变更为%s" % (slot, verbose_name, old_value, new_value)
                record_list.append(msg)
        obj.save()
        if record_list:
            models.AssetRecord.objects.create(server=server, content=';'.join(record_list))
    # 删除
    models.Disk.objects.filter(server=server, slot__in=del_disk_slot_list).delete()
    if del_disk_slot_list:
        msg = "【硬盘变更】移除槽位%s上的硬盘" % (';'.join(del_disk_slot_list))
        models.AssetRecord.objects.create(server=server, content=msg)

    # 添加
    for slot in add_disk_slot_list:
        row_dict = disk_info[slot]
        row_record_list=[]
        for name, new_value in row_dict.items():
            verbose_name = models.Disk._meta.get_field(name).verbose_name
            tpl = "%s:%s" % (verbose_name, new_value,) # 新增了那个硬盘
            row_record_list.append(tpl)

        msg = "【硬盘变更】槽位%s新增硬盘,硬盘信息：%s" % (slot, ';'.join(row_record_list),)
        models.AssetRecord.objects.create(server=server, content=msg)
        row_dict['server'] = server
        models.Disk.objects.create(**row_dict)


def process_nic(request,server):
    # 1.1 获取数据库中的硬盘信息
    nic_queryset = models.NIC.objects.filter(server=server)

    # 1.2 最新汇报来的硬盘信息
    nic_info = request.data['nic']['data']

    nic_queryset_set = {row.name for row in nic_queryset}
    nic_info_set = set(nic_info)

    update_nic_slot_list = nic_info_set & nic_queryset_set
    add_nic_slot_list = nic_info_set - nic_queryset_set
    del_nic_slot_list = nic_queryset_set - nic_info_set

    # 更新
    for nic_name in update_nic_slot_list:

        # models.NIC.objects.filter(name=name, server=server).update(**nic_info[name])
        obj = models.NIC.objects.filter(name=nic_name, server=server).first()
        row_dict = nic_info[nic_name]
        record_list = []
        for name, new_value in row_dict.items():

            old_value = str(getattr(obj, name))
            if old_value != new_value:
                setattr(obj, name, new_value)
                verbose_name = models.NIC._meta.get_field(name).verbose_name
                msg = "【网卡变更】网卡%s：%s由%s变更为%s" % (nic_name, verbose_name, old_value, new_value)
                record_list.append(msg)
        obj.save()
        if record_list:
            models.AssetRecord.objects.create(server=server, content=';'.join(record_list))
    # 删除
    # for nic_name in del_nic_slot_list:
    models.NIC.objects.filter(server=server, name__in=del_nic_slot_list).delete()
    if del_nic_slot_list:
        msg = "【网卡变更】移除网卡%s" % (';'.join(del_nic_slot_list))
        models.AssetRecord.objects.create(server=server, content=msg)

    # 添加
    for nic_name in add_nic_slot_list:
        row_dict = nic_info[nic_name]
        row_record_list = []
        for name, new_value in row_dict.items():
            verbose_name = models.NIC._meta.get_field(name).verbose_name
            tpl = "%s:%s" % (verbose_name, new_value,)
            row_record_list.append(tpl)

        msg = "【网卡变更】新增网卡%s,网卡信息：%s" % (nic_name, ';'.join(row_record_list),)
        models.AssetRecord.objects.create(server=server, content=msg)
        row_dict['server'] = server
        row_dict['name'] = nic_name
        models.NIC.objects.create(**row_dict)


def process_memory(request,server):
    # 1.1 获取数据库中的内存信息
    memory_queryset = models.Memory.objects.filter(server=server)

    # 1.2 最新汇报来的内存信息
    memory_info = request.data['memory']['data']

    memory_queryset_set = {row.slot for row in memory_queryset}
    memory_info_set = set(memory_info)

    update_memory_slot_list = memory_info_set & memory_queryset_set
    add_memory_slot_list = memory_info_set - memory_queryset_set
    del_memory_slot_list = memory_queryset_set - memory_info_set

    # 更新
    for slot in update_memory_slot_list:
        models.Memory.objects.filter(slot=slot, server=server).update(**memory_info[slot])
    # 删除
    models.Memory.objects.filter(server=server, slot__in=del_memory_slot_list).delete()

    # 添加
    for slot in add_memory_slot_list:
        row_dict = memory_info[slot]
        row_dict['server'] = server
        models.Memory.objects.create(**row_dict)