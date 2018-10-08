"""RTF URL Configuration

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
from RTF import settings
from app01 import views
from django.views.static import serve  # 用户上传文件用的模块
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 给用户上传的那些文件路径做认证上传头像的
    url(r'^media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),
    # 富文本编辑器
    url(r'^fault-report/upload-img/$', views.upload_img),
    url(r'^index/$', views.index),
]
