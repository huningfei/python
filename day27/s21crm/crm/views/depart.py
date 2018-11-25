from django.shortcuts import render, redirect
from crm import models
from crm.forms.depart import DepartModelForm
from django.urls import reverse


def depart_list(request):
    """
    部门列表
    :param request:
    :return:
    """
    queryset = models.Department.objects.all()
    return render(request, 'depart_list.html', {'queryset': queryset})


def depart_add(request):
    """
    部门添加
    :param request:
    :return:
    """

    if request.method == "GET":
        form = DepartModelForm()
        return render(request, 'depart_add.html', {'form': form})

    form = DepartModelForm(data=request.POST)
    if form.is_valid():
        form.save()

        return redirect('depart_list')
    else:
        return render(request, 'depart_add.html', {'form': form})


def depart_edit(request, nid):
    """
    编辑部门
    :param request:
    :param nid:
    :return:
    """
    obj = models.Department.objects.filter(id=nid).first()
    if request.method == "GET":
        form = DepartModelForm(instance=obj) # 加上instance才能在编辑页面显示原来的数据
        return render(request, 'depart_edit.html', {"form": form})
    form = DepartModelForm(data=request.POST, instance=obj) # data是把编辑好的数据提交过去
    if form.is_valid():
        form.save()
        return redirect('depart_list')
    else:
        return render(request, 'depart_edit.html', {"form": form})
def depart_del(request,nid):
    """
    删除用户
    :param request:
    :param nid:
    :return:
    """
    models.Department.objects.filter(id=nid).delete()
    return redirect('depart_list')

