from django.conf.urls import url, include
from web.views import home

urlpatterns = [
    url(r'^add_user/', home.add_user),
    url(r'^info/', home.info),
    url(r'^del_user/(\d+)/$', home.del_user),
    url(r'^edit_user/(\d+)/$', home.edit_user),
    url(r'^user/', home.userlist),
    url(r'^add_order/', home.add_order),
    url(r'^orderlist/', home.orderlist),
    url(r'^orderinfo/', home.orderinfo),
    url(r'^del_order/(\d+)/$', home.del_order),
    url(r'^edit_order/(\d+)/$', home.edit_order),
]
