from django.db import models


# Create your models here.

# 建表出版社
class Publisher(models.Model):
    name = models.CharField(max_length=22)


# 书籍表关联出版社
class Book(models.Model):
    title = models.CharField(max_length=32)
    publisher = models.ForeignKey(to="Publisher", on_delete=models.CASCADE)


# 人员表
class Person(models.Model):
    name = models.CharField(max_length=22)
    age = models.IntegerField()
    birthday = models.DateField()
    birthday2 = models.DateTimeField(null=True)
    phone = models.CharField(max_length=11, unique=True)
    # 创建该记录时自动把当前时间保存到该字段
    join_date = models.DateField(auto_now_add=True)
    # 更新该记录的值时 自动把当前时间保存到该字段
    last_date = models.DateField(auto_now=True)

    def __str__(self):
        return "{}-{}".format(self.name, self.age, self.phone)
