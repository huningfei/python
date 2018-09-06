from django.conf.urls import url
from fault_reporting import views

urlpatterns = [

    # 第一版， 特别low版
    # url('^lob/(.*)/$', views.lob),
    # url('^tag/(.*)/$', views.tag),
    # url('^archive/(.*)/$', views.archive),
    #
    # # 第二版： 三合一
    # url(r'(lob|tag|archive)/(.*)/$', views.sanhe1),  # sanhe1(request, *args)  args[0]=="lob"

    # 第三版： 四合一
    url(r'(lob|tag|archive)/(.*)/$', views.index),  # index(request, "lob", "游戏")

    url('^$', views.index),  # index(request)
]