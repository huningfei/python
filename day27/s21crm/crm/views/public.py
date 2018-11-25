from django.shortcuts import render, redirect
from crm import models
from crm.forms.public import PublicCustomModelForm
from django.urls import reverse


def public_customer_list(request):
    """
    公户列表
    :param request:
    :return:
    """
    if request.method == "POST":  # 当用户点击申请到私户的时候执行下面代码
        id_list = request.POST.getlist('pk')  # 获取客户id
        current_user_id = request.session['user_info']['id']  # 获取当前登录用户id
        # 找到公户，并且把公户的课程顾问设置成当前登录用户
        models.Customer.objects.filter(id__in=id_list).update(consultant_id=current_user_id)
        # 如果是get就查找公户，就是没有课程顾问的用户
    queryset = models.Customer.objects.filter(consultant__isnull=True)  # 课程顾问等于空
    return render(request, 'public_custom_list.html', {'queryset': queryset})


def public_customer_add(request):
    """
    部门添加
    :param request:
    :return:
    """

    if request.method == "GET":
        form = PublicCustomModelForm()
        return render(request, 'public_custom_add.html', {'form': form})

    form = PublicCustomModelForm(data=request.POST)
    if form.is_valid():
        form.save()

        return redirect('public_customer_list')
    else:
        return render(request, 'public_custom_add.html', {'form': form})


def public_customer_edit(request, nid):
    """
    编辑部门
    :param request:
    :param nid:
    :return:
    """
    obj = models.Customer.objects.filter(id=nid).first()
    if request.method == "GET":
        form = PublicCustomModelForm(instance=obj)  # 加上instance才能在编辑页面显示原来的数据
        return render(request, 'public_custom_edit.html', {"form": form})
    form = PublicCustomModelForm(data=request.POST, instance=obj)  # data是把编辑好的数据提交过去
    if form.is_valid():
        form.save()
        return redirect('public_customer_list')
    else:
        return render(request, 'public_custom_edit.html', {"form": form})


def public_customer_del(request, nid):
    """
    删除用户
    :param request:
    :param nid:
    :return:
    """
    models.Customer.objects.filter(id=nid).delete()
    return redirect('public_customer_list')
