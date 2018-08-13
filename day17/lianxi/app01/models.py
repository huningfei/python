from django.db import models

# Create your models here.

#建表
class Publisher(models.Model):
    name=models.CharField(max_length=22)
