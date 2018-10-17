from django.conf.urls import url,include
from web.views import home

urlpatterns = [
    url(r'^add_user/', home.add_user),
    url(r'^add_order/', home.add_order),
    url(r'^user/', home.userlist),
    url(r'^orderlist/', home.orderlist),
]
