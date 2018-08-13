import os
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lianxi.settings")
    import django
    django.setup()

from app01 import models
# 查询一个
# ret = models.Person.objects.get(age=18)
# print(ret)
# 查询所有
# ret1 = models.Person.objects.filter(age=18)
# print(ret1)
#
# ret2 = models.Person.objects.filter(age=18).values("age", "phone","name")
# print(ret2)
#
# ret3 = models.Person.objects.filter(age=18).values_list("age", "phone",'name')
# print(ret3)

# 排序
# ret = models.Person.objects.all().order_by("age")
# print(ret)

# 查询大于18的
# ret1 = models.Person.objects.filter(age__gt=18)
# print(ret1)

# 查询id在【1,2】的人
# ret = models.Person.objects.filter(id__in=[1,2])
# print(ret)

# 查询id不在【1,2】
# ret = models.Person.objects.exclude(id__in=[1,2])
# print(ret)

# 查询名字中包含jj的那个人(不区分大小写)
# ret = models.Person.objects.filter(name__contains="JJ")
# print(ret)

# 查询id在1-3区间内的数据
# ret = models.Person.objects.filter(id__range=[1, 3])
# print(ret)

# 查询以JJ结尾的人
# ret = models.Person.objects.filter(name__endswith='JJ')
# print(ret)

# 查询生日在2018年的，（sqlit查不到）
ret = models.Person.objects.filter(birthday__year=2018)
print(ret)