from django.shortcuts import render, redirect
from rbac import models
from rbac.forms.permission import PermissionModelForm
from django.urls import reverse


def permission_list(request):
    """
    部门列表
    :param request
    :return:
    """
    queryset = models.Permission.objects.all()
    return render(request, 'permission_list.html', {'queryset': queryset})


def permission_add(request):
    """
    部门添加
    :param request:
    :return:
    """

    if request.method == "GET":
        form = PermissionModelForm()
        return render(request, 'permission_add.html', {'form': form})

    form = PermissionModelForm(data=request.POST)
    if form.is_valid():
        form.save()

        return redirect('permission_list')
    else:
        return render(request, 'permission_add.html', {'form': form})


def permission_edit(request, nid):
    """
    编辑部门
    :param request:
    :param nid:
    :return:
    """
    obj = models.Permission.objects.filter(id=nid).first()
    if request.method == "GET":
        form = PermissionModelForm(instance=obj)  # 加上instance才能在编辑页面显示原来的数据
        return render(request, 'permission_edit.html', {"form": form})
    form = PermissionModelForm(data=request.POST, instance=obj)  # data是把编辑好的数据提交过去
    if form.is_valid():
        form.save()
        return redirect('permission_list')
    else:
        return render(request, 'permission_edit.html', {"form": form})


def permission_del(request, nid):
    """
    删除用户
    :param request:
    :param nid:
    :return:
    """
    models.Permission.objects.filter(id=nid).delete()
    return redirect('permission_list')
