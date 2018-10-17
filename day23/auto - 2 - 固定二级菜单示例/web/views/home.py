from django.shortcuts import render, redirect
from web import models
from web.forms import  UserForm


# from django.conf import settings


def add_user(request):
    form_obj=UserForm()
    if request.method == "POST":
        form_obj=UserForm(request.POST)
        print(form_obj)
        if form_obj.is_valid():
            models.User.objects.create(form_obj)
            return redirect("/web/user/")
    return render(request,"add_user.html",locals())



def add_order(request):
    # menus = settings.MENU_LIST

    return render(request, 'add_order.html')


def userlist(request):
    data = models.User.objects.all
    return render(request, 'userlist.html', {'user_list': data})


def orderlist(request):
    return render(request, 'orderlist.html')
