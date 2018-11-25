from django.db import models



# Create your models here.


# 用户表
class UserInfo(models.Model):
    username = models.CharField(max_length=16, verbose_name="用户名")
    password = models.CharField(max_length=32, verbose_name="密码")
    roles = models.ManyToManyField(to="Role", null=True, blank=True)
    # null=TRUE是告诉数据库这个字段可以为空，blank=True告诉djangoadmin可以不填

    # 显示具体的内容
    def __str__(self):
        return self.username

    # 让字段显示中文
    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name


# 角色
class Role(models.Model):
    title = models.CharField(max_length=32, verbose_name="角色名称")
    permissions = models.ManyToManyField(to="Permission")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "角色表"
        verbose_name_plural = verbose_name


# 权限表
class Permission(models.Model):
    title = models.CharField(max_length=16, verbose_name="权限名称")
    url = models.CharField(max_length=255, verbose_name="URL")
    is_menu = models.BooleanField(default=False, verbose_name="可作为菜单展示")
    icon = models.CharField(max_length=16, verbose_name="菜单图标", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "权限表"
        verbose_name_plural = verbose_name

