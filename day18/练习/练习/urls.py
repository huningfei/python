"""练习 URL Configuration

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

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # session 验证
    url(r'^login/$', views.login),
    url(r'^index/$', views.index),
    url(r'^secode/$', views.secode),
    # 分页功能
    url(r'^book_list/$', views.book_list),
    url(r'^publisher_list/$', views.publisher_list),
    # 中间件
    url(r'^test/$', views.test),
    # orm多对多
    url(r'^author_list/$',views.author_list),
    url(r'^add_author/$',views.Addauthor.as_view()),
    # 编辑
    url(r'^edit_author/(\d+)/$',views.Editauthor.as_view()),
    # 删除
    url(r'^del_author/(\d+)/$',views.del_author),
    # ajax
    url(r'^ajax_test/$',views.ajax_test),
    url(r'^calc/$',views.calc),
    # 注册
    url(r'^reg/$',views.reg),
    url(r'^check_username/$',views.check_username),
]
