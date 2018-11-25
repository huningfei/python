from django.shortcuts import render, redirect
from rbac import models
from rbac.forms.meau import MenuModelForm
from django.urls import reverse


def menu_list(request):
    """
    部门列表
    :param request:
    :return:
    """
    queryset = models.Menu.objects.all()
    return render(request, 'menu_list.html', {'queryset': queryset})


def menu_add(request):
    """
    部门添加
    :param request:
    :return:
    """

    if request.method == "GET":
        form = MenuModelForm()
        return render(request, 'menu_add.html', {'form': form})

    form = MenuModelForm(data=request.POST)
    if form.is_valid():
        form.save()

        return redirect('menu_list')
    else:
        return render(request, 'menu_add.html', {'form': form})


def menu_edit(request, nid):
    """
    编辑部门
    :param request:
    :param nid:
    :return:
    """
    obj = models.Menu.objects.filter(id=nid).first()
    if request.method == "GET":
        form = MenuModelForm(instance=obj)  # 加上instance才能在编辑页面显示原来的数据
        return render(request, 'menu_edit.html', {"form": form})
    form = MenuModelForm(data=request.POST, instance=obj)  # data是把编辑好的数据提交过去
    if form.is_valid():
        form.save()
        return redirect('menu_list')
    else:
        return render(request, 'menu_edit.html', {"form": form})


def menu_del(request, nid):
    """
    删除用户
    :param request:
    :param nid:
    :return:
    """
    models.Menu.objects.filter(id=nid).delete()
    return redirect('menu_list')
