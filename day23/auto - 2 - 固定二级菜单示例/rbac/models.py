from django.db import models


class User(models.Model):
    '''
    用户表
    '''
    name = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    roles = models.ManyToManyField(verbose_name='关联角色', to="Role", null=True, blank=True)


class Role(models.Model):
    '''
    角色表
    '''
    role = models.CharField(verbose_name='角色名', max_length=32)
    permissions = models.ManyToManyField(verbose_name='关联权限', to="Permission")


class Menu(models.Model):
    '''
    菜单表
    '''
    title = models.CharField(verbose_name='菜单名字', max_length=64)
    icon = models.CharField(verbose_name='图标名称', max_length=128)


class Permission(models.Model):
    '''
    权限表
    '''
    url = models.CharField(verbose_name='url(含正则)', max_length=128)
    title = models.CharField(verbose_name='菜单名字', max_length=64)
    name = models.CharField(verbose_name='url别名', max_length=64, unique=True)
    menu = models.ForeignKey(verbose_name='关联菜单表', to='Menu', null=True, blank=True)
    # null数据库可以为空，blank django是空
    parent = models.ForeignKey(verbose_name='父菜单', to='Permission', null=True, blank=True)
