from django.contrib import admin
from rbac import models
admin.site.register(models.UserInfo)
admin.site.register(models.Role)
# Register your models here.
