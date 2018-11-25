from django.shortcuts import render, redirect
from crm import models
from crm.forms.user import UserInfoModelForm
from django.urls import reverse


def user_list(request):
    """
    部门列表
    :param request:
    :return:
    """
    queryset = models.UserInfo.objects.all()
    return render(request, 'user_list.html', {'queryset': queryset})


def user_add(request):
    """
    部门添加
    :param request:
    :return:
    """

    if request.method == "GET":
        form = UserInfoModelForm()
        return render(request, 'user_add.html', {'form': form})

    form = UserInfoModelForm(data=request.POST)
    if form.is_valid():
        form.save()

        return redirect('user_list')
    else:
        return render(request, 'user_add.html', {'form': form})


def user_edit(request, nid):
    """
    编辑部门
    :param request:
    :param nid:
    :return:
    """
    obj = models.UserInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        form = UserInfoModelForm(instance=obj)  # 加上instance才能在编辑页面显示原来的数据
        return render(request, 'user_edit.html', {"form": form})
    form = UserInfoModelForm(data=request.POST, instance=obj)  # data是把编辑好的数据提交过去
    if form.is_valid():
        form.save()
        return redirect('user_list')
    else:
        return render(request, 'user_edit.html', {"form": form})


def user_del(request, nid):
    """
    删除用户
    :param request:
    :param nid:
    :return:
    """
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('user_list')
