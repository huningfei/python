from repository import models


class Disk(object):
    def __init__(self, server_obj, info):
        '''

        :param server_obj: 主机名
        :param info: 硬盘信息
        '''
        self.server_obj = server_obj
        self.disk_dict = info

    def process(self):
        new_disk_info_dict = self.disk_dict['data']  # 客户端发送过来新的数据


        """
        新的数据格式是字典
        {
        '0': {'slot': '0', 'pd_type': 'SAS', 'capacity': '279.396', 'model': 'SEAGATE ST300MM0006     LS08S0K2B5NV'}, 
        '1': {'slot': '1', 'pd_type': 'SAS', 'capacity': '279.396', 'model': 'SEAGATE ST300MM0006     LS08S0K2B5AH'}, 
        '2': {'slot': '2', 'pd_type': 'SATA', 'capacity': '476.939', 'model': 'S1SZNSAFA01085L  

        }
        """
        new_disk_info_list = self.server_obj.disk.all()
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
        print(update_slot_list)
        # 增加
        add_record_list = []
        for slot in add_slot_list:  # slot是key
            value = new_disk_info_dict[slot]  # 根据key获得value
            tmp = "添加硬盘"
            add_record_list.append(tmp)
            value['server_obj'] = self.server_obj
            models.Disk.objects.create(**value)
        # 删除 包含在del_slot_list里面的全部删除掉
        models.Disk.objects.filter(server_obj=self.server_obj, slot__in=del_slot_list).delete()

        # 更新
        # record_list = []  # 定义一个更改列表
        for slot in update_slot_list:
            # print(slot)
            value = new_disk_info_dict[slot]  # slot': '0', 'pd_type': 'SAS', 'capacity': '279.396', 'model': 'SEAGATE ST300MM0006     LS08S0K2B5NV'
            obj = models.Disk.objects.filter(server_obj=self.server_obj, slot=slot).first()
            # print('我是更新里面的obj',obj)
            for k, new_val in value.items():
                old_val = getattr(obj, k)
                # print(old_val)

                if old_val != new_val:
                    # record = "[%s]的[%s]里面的[%s]由[%s]变更为[%s]" % (self.server_obj.hostname, slot, k, old_val, new_val)
                    # print(record)
                    # record_list.append(record)
                    # print(record_list)
                    setattr(obj, k, new_val)
            obj.save()


        # if record_list:
        #     models.ServerRecord.objects.create(server_obj=self.server_obj, content=';'.join(record_list))


