#!/usr/bin/python
# -*- coding:utf-8 -*-

disk_info = {
    '#1':{'factory':'x1','model':'x2','size':600},
    '#2':{'factory':'x1','model':'x2','size':500},
    '#3':{'factory':'x1','model':'x2','size':600},
    '#4':{'factory':'x1','model':'x2','size':900},
}


disk_queryset = [
    {'slot':'#1','factory':'x1','model':'x2','size':600},
    {'slot':'#2','factory':'x1','model':'x2','size':100},
    {'slot':'#6','factory':'x1','model':'x2','size':300},
]
disk_info_set = set(disk_info)
disk_queryset_set = { row['slot'] for row in disk_queryset }
# 找到disk_info有，disk_queryset 无    ---> 应该新增硬盘
r1 = disk_info_set-disk_queryset_set
print(r1)

# 找到disk_queryset有，disk_info无     ---> 应该删除硬盘
r2 = disk_queryset_set - disk_info_set
print(r2)

# 找到disk_info有，disk_queryset 有    ---> 应该更新的硬盘
r3 = disk_queryset_set & disk_info_set
print(r3)