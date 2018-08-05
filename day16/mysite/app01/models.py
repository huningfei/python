from django.db import models

# Create your models here.

# 所有和数据库ORM相关的类都在这个文件定义，并且只能在这个文件定义


# 定义一个 出版社 类
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    
    def __str__(self):
        return self.name
