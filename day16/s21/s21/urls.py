"""s21 URL Configuration

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
    url(r'^index/', views.index),
    url(r'^home/', views.home),
    url(r'^login/', views.login),
    #出版社列表
    url(r'^publisher_list',views.publisher_list),
    #添加出版社
    url(r'^add_publisher',views.add_publisher),
    #删除出版社
    url(r'^del_publisher',views.del_publisher),
    #编辑出版社
    url(r'^edit_publisher/',views.edit_publisher),
]
