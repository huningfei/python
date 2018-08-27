from django.db import models

# Create your models here.
class Publisher(models.Model):
    name=models.CharField(max_length=32,unique=True,verbose_name="出版社名字") # 字段显示中文需要用verbose_name
    address=models.TextField(verbose_name="出版社地址")

    def __str__(self): # 页面显示详细信息需要写这个
        return self.name

    class Meta:   # 表名显示中文
        verbose_name="出版社"
        verbose_name_plural=verbose_name # 复数的意思，如果不加这个后面会多个s

class Author(models.Model):
    name=models.CharField(max_length=12)
    gender=models.SmallIntegerField(
        choices=((0,"女"),(1,"男"),(2,"保密")),
        default=2
    )
    age=models.IntegerField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="作者"
        verbose_name_plural = verbose_name


class Book(models.Model):
    title=models.CharField(max_length=32,unique=True)
    publisher_date=models.DateField(auto_now_add=True)
    phone=models.CharField(max_length=11,unique=True,null=True,blank=True) # blank可以不填
    publisher=models.ForeignKey(to="Publisher",on_delete=models.CASCADE) # 外键
    authors=models.ManyToManyField(to="Author") # 多对多

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "书名"
        verbose_name_plural = verbose_name