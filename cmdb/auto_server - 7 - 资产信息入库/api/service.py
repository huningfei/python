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
        models.Disk.objects.filter(slot=slot, server=server).update(**disk_info[slot])
    # 删除
    models.Disk.objects.filter(server=server, slot__in=del_disk_slot_list).delete()

    # 添加
    for slot in add_disk_slot_list:
        row_dict = disk_info[slot]
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
    for name in update_nic_slot_list:
        models.NIC.objects.filter(name=name, server=server).update(**nic_info[name])
    # 删除
    models.NIC.objects.filter(server=server, name__in=del_nic_slot_list).delete()

    # 添加
    for name in add_nic_slot_list:
        row_dict = nic_info[name]
        row_dict['server'] = server
        row_dict['name'] = name
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