
from django.conf.urls import url,include
from django.contrib import admin
from app01 import views
urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^user/$', views.user_list),
    url(r'^user/add/$', views.user_add),
    url(r'^user/edit/(\d+)/$', views.user_edit),
    url(r'^user/del/(\d+)$', views.user_del),
    
    url(r'^center/$', views.center),
]

