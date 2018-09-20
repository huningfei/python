from django.contrib import admin
from rbac import models
admin.site.register(models.UserInfo)
admin.site.register(models.Role)

# Register your models here.
# 自定义一个权限管理类
class PermissionAdmin(admin.ModelAdmin):
    # 告诉django admin在页面上展示我这张表的那些字段
    list_display = ["title","url","is_menu","icon"]
    # 在列表页面可以编辑url
    list_editable = ["url","icon","is_menu"]


admin.site.register(models.Permission,PermissionAdmin)

