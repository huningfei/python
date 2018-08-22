from django.db import models

# Create your models here.
#创建用户库
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=32,unique=True)
    password=models.CharField(max_length=32)
    services=models.ManyToManyField(to="Service",related_name="user")

# 创建业务表
class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=32,unique=True)

# 创建主机表
class Host(models.Model):
    id = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32)
    pwd=models.CharField(max_length=32)
    service=models.ForeignKey(to="Service",on_delete=models.CASCADE)





