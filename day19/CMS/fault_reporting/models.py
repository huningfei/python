from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserInfo(AbstractUser):
    phone=models.CharField(max_length=11)
    avatar=models.FileField(upload_to="avatars/",default="avatars/default.png")
