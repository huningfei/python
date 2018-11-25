from django.db import models


# Create your models here.
class User(models.Model):
    '''
    用户表
    '''
    name = models.CharField(verbose_name='姓名', max_length=32)


class Order(models.Model):
    '''
    订单表
    '''
    name = models.CharField(verbose_name='名字', max_length=32)
