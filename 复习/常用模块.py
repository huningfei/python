# orderedict有序字典
import collections
# d = collections.OrderedDict()
#
# d['苹果'] = 10
# d['手机']=5000
# print(d)
# for i in d:
#     print(i,d[i])

# defaultdict 默认字典
#
# 例子：小于66的放到k2，大于66的放到k1,形成一个新字典
from collections import defaultdict
l= [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
new_dict = defaultdict(list)
for value in l:
    if value > 66:
        new_dict['k1'].append(value)
    else:
        new_dict['k2'].append(value)
print(new_dict)