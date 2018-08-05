"""mysite URL Configuration

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
# from . import views
from app01 import views

# 用户访问的URL和将要执行的函数的对应关系
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    # url(r'^index/hehe/', views.index),
    url(r'^login/$', views.login),
    # 出版社列表页
    url(r'publisher_list/', views.publisher_list),
    # 添加出版社
    url(r'add_publisher/', views.add_publisher),
    # 删除出版社
    url(r'delete_publisher/', views.delete_publisher),
    # 编辑出版社
    url(r'edit_publisher/', views.edit_publisher),

]
