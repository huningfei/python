"""s21crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from crm.views import depart
from crm.views import userinfo
from crm.views import course
from crm.views import school
from crm.views import classes
from crm.views import public
from crm.views import private
from crm.views import login
from crm.views import logout
from crm.views import record
from rbac.views import menu
from rbac.views import permission
from rbac.views import role

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login.login, name="login"),
    url(r'^logout/', login.logout, name="logout"),
    url(r'^index/', login.index, name="index"),
    # 部门
    url(r'^depart/list/', depart.depart_list, name='depart_list'),
    url(r'^depart/add/', depart.depart_add, name='depart_add'),
    url(r'^depart/edit/(\d+)', depart.depart_edit, name='depart_edit'),
    url(r'^depart/del/(\d+)', depart.depart_del, name='depart_del'),
    # 用户
    url(r'^user/list/', userinfo.user_list, name='user_list'),
    url(r'^user/add/', userinfo.user_add, name='user_add'),
    url(r'^user/edit/(\d+)/', userinfo.user_edit, name='user_edit'),
    url(r'^user/del/(\d+)/', userinfo.user_del, name='user_del'),
    # 课程
    url(r'^course/list/', course.course_list, name='course_list'),
    url(r'^course/add/', course.course_add, name='course_add'),
    url(r'^course/edit/(\d+)/', course.course_edit, name='course_edit'),
    url(r'^course/del/(\d+)', course.course_del, name='course_del'),
    # 学校
    url(r'^school/list/', school.school_list, name='school_list'),
    url(r'^school/add/', school.school_add, name='school_add'),
    url(r'^school/edit/(\d+)', school.school_edit, name='school_edit'),
    url(r'^school/del/(\d+)', school.school_del, name='school_del'),
    # 班级

    url(r'^classes/list/', classes.classes_list, name='classes_list'),
    url(r'^classes/add/', classes.classes_add, name='classes_add'),
    url(r'^classes/edit/(\d+)', classes.classes_edit, name='classes_edit'),
    url(r'^classes/del/(\d+)', classes.classes_del, name='classes_del'),

    # 公户管理
    url(r'^public/custom/list/', public.public_customer_list, name='public_customer_list'),
    url(r'^public/custom/add/', public.public_customer_add, name='public_customer_add'),
    url(r'^public/custom/edit/(\d+)', public.public_customer_edit, name='public_customer_edit'),
    url(r'^public/custom/del/(\d+)', public.public_customer_del, name='public_customer_del'),

    # 私户管理
    url(r'^private/custom/list/', private.private_customer_list, name='private_customer_list'),
    url(r'^private/custom/add/', private.private_customer_add, name='private_customer_add'),
    url(r'^private/custom/edit/(\d+)', private.private_customer_edit, name='private_customer_edit'),

    # 跟进记录

    url(r'^record/list/(\d+)/', record.record_list, name='record_list'),
    url(r'^record/add/(\d+)/', record.record_add, name='record_add'),

    # 菜单
    url(r'^menu/list/', menu.menu_list, name='menu_list'),
    url(r'^menu/add/', menu.menu_add, name='menu_add'),
    url(r'^menu/edit/(\d+)/', menu.menu_edit, name='menu_edit'),
    url(r'^menu/del/(\d+)/', menu.menu_del, name='menu_del'),

    # 权限
    url(r'^permission/list/', permission.permission_list, name='permission_list'),
    url(r'^permission/add/', permission.permission_add, name='permission_add'),
    url(r'^permission/edit/(\d+)/', permission.permission_edit, name='permission_edit'),
    url(r'^permission/del/(\d+)/', permission.permission_del, name='permission_del'),
    # 角色
    url(r'^role/list/', role.role_list, name='role_list'),
    url(r'^role/add/', role.role_add, name='role_add'),
    url(r'^role/edit/(\d+)/', role.role_edit, name='role_edit'),
    url(r'^role/del/(\d+)/', role.role_del, name='role_del'),

]
