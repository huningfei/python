from django.shortcuts import render
from web import models

# from django.conf import settings


def add_user(request):
    # menus = settings.MENU_LIST

    return render(request, 'add_user.html')


def add_order(request):
    # menus = settings.MENU_LIST

    return render(request, 'add_order.html')


def userlist(request):
    data=models.User.objects.all
    return render(request, 'userlist.html',{'user_list':data})


def orderlist(request):
    return render(request, 'orderlist.html')
