"""lianxi URL Configuration

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
from app01 import views



urlpatterns =  [
    url(r'^admin/', admin.site.urls),
    url(r'^publisher_list/$', views.publisher_list,name="list"),
    # 动态传参-FBV
    # url(r'^edit_publisher/(\d+)/$', views.edit_publisher),
    # 动态传参-CBV
    url(r'^edit_publisher/(?P<edit_id>\d+)/$', views.EditPublisher.as_view(), name="wusir"),
    # url传参
    # url(r'^edit_publisher/$', views.edit_publisher),
    # 上传文件
    url(r'^upload/$', views.upload.as_view()),
    # 测试返回Json格式数据
    url(r'^json_test/$', views.JsonTest.as_view()),
    # 测试模板语法
    url(r'^template_test/$', views.template_test),
    #  测试跨站请求伪造 （CSRF）
    url(r'^csrf_test/$', views.csrf_test),

    # 外键增删改查
    # 查看列表
    url(r'^book_list/$', views.book_list),
    # 增加
    url(r'^add_list/$', views.add_list,name="add_book"),

    # 删除
    url(r'^del_book/(?P<pk>\d+)$', views.del_book, name="del_book"),
    # 编辑
    url(r'^edit_book/(?P<pk>\d+)$', views.edit_book, name="edit_book"),
    # 登录设置cookie
    url(r'^login/$', views.login),





]
