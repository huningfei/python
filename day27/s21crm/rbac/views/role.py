from django.shortcuts import render, redirect
from rbac import models
from rbac.forms.role import RoleModelForm



def role_list(request):
    """
    部门列表
    :param request:
    :return:
    """
    queryset = models.Role.objects.all()
    return render(request, 'role_list.html', {'queryset': queryset})


def role_add(request):
    """
    部门添加
    :param request:
    :return:
    """

    if request.method == "GET":
        form = RoleModelForm()
        return render(request, 'role_add.html', {'form': form})

    form = RoleModelForm(data=request.POST)
    if form.is_valid():
        form.save()

        return redirect('role_list')
    else:
        return render(request, 'role_add.html', {'form': form})


def role_edit(request, nid):
    """
    编辑部门
    :param request:
    :param nid:
    :return:
    """
    obj = models.Role.objects.filter(id=nid).first()
    if request.method == "GET":
        form = RoleModelForm(instance=obj)  # 加上instance才能在编辑页面显示原来的数据
        return render(request, 'role_edit.html', {"form": form})
    form = RoleModelForm(data=request.POST, instance=obj)  # data是把编辑好的数据提交过去
    if form.is_valid():
        form.save()
        return redirect('role_list')
    else:
        return render(request, 'role_edit.html', {"form": form})


def role_del(request, nid):
    """
    删除用户
    :param request:
    :param nid:
    :return:
    """
    models.Role.objects.filter(id=nid).delete()
    return redirect('role_list')
