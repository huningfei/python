from django.shortcuts import render, redirect
from web import models
from web.forms import UserForm
from web.modelform import OrderModelForm




def add_user(request):
    form_obj = UserForm()
    username = request.POST.get("name")
    # print(username)

    if request.method == "POST":
        form_obj = UserForm(request.POST)
        if form_obj.is_valid():  # 校验数据有效性
            old_name = models.User.objects.filter(name=username)
            if old_name:
                data = "用户名已经存在"
                return render(request, "add_user.html", locals())
            else:
                models.User.objects.create(**form_obj.cleaned_data)
                return redirect("/web/user/")
    return render(request, "add_user.html", locals())


def del_user(request, pk):
    models.User.objects.filter(id=pk).delete()
    return redirect("/web/user/")


def edit_user(request, pk):
    username = request.POST.get("name")
    user_obj = models.User.objects.filter(id=pk).first()

    from django.forms import model_to_dict
    user_dict = model_to_dict(user_obj)
    form_obj = UserForm(user_dict)
    if request.method == "POST":
        form_obj = UserForm(request.POST)
        if form_obj.is_valid():
            old_name = models.User.objects.filter(name=username)
            if old_name:
                data = "用户名已经存在"
                return render(request, "edit_user.html", locals())
            user_obj.name = form_obj.cleaned_data.get("name")
            user_obj.save()
            return redirect("/web/user/")
    return render(request, "edit_user.html", locals())


def info(requst):
    return render(requst, "user_info.html")


def userlist(request):
    data = models.User.objects.all
    return render(request, 'userlist.html', {'user_list': data})


# from django.forms import ModelForm
#
#
# class OrderModelForm(ModelForm):
#     class Meta:
#         model = models.Order
#         fields = "__all__"


def add_order(request):
    if request.method == "GET":
        form = OrderModelForm()
    else:
        form = OrderModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/web/orderlist")

    return render(request, 'add_order.html', {'form': form})


def orderlist(request):
    data = models.Order.objects.all
    return render(request, 'orderlist.html', {'order_list': data})


def orderinfo(requst):
    return render(requst, "orderinfo.html")


def edit_order(request, pk):
    obj = models.Order.objects.filter(id=pk).first()
    print(obj)
    if request.method == "GET":
        form = OrderModelForm(instance=obj)
        return render(request, 'edit_order.html', {"form": form})
    else:
        form = OrderModelForm(instance=obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/web/orderlist/")
        return render(request, "edit_order.html", {"form": form})


def del_order(request, uid):
    models.Order.objects.filter(id=uid).delete()
    return redirect("/web/orderlist/")
