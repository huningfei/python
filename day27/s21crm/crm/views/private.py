from django.shortcuts import render, redirect
from crm import models
from crm.forms.private import ParivateCustomModelForm
from django.urls import reverse


def private_customer_list(request):
    """
    私户列表
    :param request:
    :return:
    """
    if request.method == "POST":  # 当用户点击申请到私户的时候执行下面代码
        id_list = request.POST.getlist('pk')  # 获取客户id

        # 找到私户，并且把当前的私户剔除到公户
        models.Customer.objects.filter(id__in=id_list).update(consultant_id=None)
    current_user_id = request.session['user_info']['id']  # 获取当前登录用户id
    queryset = models.Customer.objects.filter(consultant=current_user_id).order_by('-status')  # 查询当前用户的客户，并且按照报名状态倒叙
    return render(request, 'private_custom_list.html', {'queryset': queryset})


def private_customer_add(request):
    """
    私户添加
    :param request:
    :return:
    """

    if request.method == "GET":
        form = ParivateCustomModelForm()
        return render(request, 'private_custom_add.html', {'form': form})

    form = ParivateCustomModelForm(data=request.POST)
    if form.is_valid():
        # 课程顾问自己添加客户的时候,默认就是私户
        form.instance.consultant_id = request.session['user_info']['id']  # 把课程顾问id设置成当前登录用户的id
        form.save()

        return redirect('private_customer_list')
    else:
        return render(request, 'private_custom_add.html', {'form': form})


def private_customer_edit(request, nid):
    """
    编辑私户
    :param request:
    :param nid:
    :return:
    """
    obj = models.Customer.objects.filter(id=nid).first()
    if request.method == "GET":
        form = ParivateCustomModelForm(instance=obj)  # 加上instance才能在编辑页面显示原来的数据
        return render(request, 'private_custom_edit.html', {"form": form})
    form = ParivateCustomModelForm(data=request.POST, instance=obj)  # data是把编辑好的数据提交过去
    if form.is_valid():

        form.save()
        return redirect('private_customer_list')
    else:
        return render(request, 'private_custom_edit.html', {"form": form})
