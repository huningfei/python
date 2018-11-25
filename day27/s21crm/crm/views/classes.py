from django.shortcuts import render, redirect
from crm import models
from crm.forms.classes import ClassesModelForm
from django.urls import reverse


def classes_list(request):
    """
    部门列表
    :param request:
    :return:
    """
    queryset = models.ClassList.objects.all()
    return render(request, 'classes_list.html', {'queryset': queryset})


def classes_add(request):
    """
    部门添加
    :param request:
    :return:
    """

    if request.method == "GET":
        form = ClassesModelForm()
        return render(request, 'classes_add.html', {'form': form})

    form = ClassesModelForm(data=request.POST)
    if form.is_valid():
        form.save()

        return redirect('classes_list')
    else:
        return render(request, 'classes_add.html', {'form': form})


def classes_edit(request, nid):
    """
    编辑部门
    :param request:
    :param nid:
    :return:
    """
    obj = models.ClassList.objects.filter(id=nid).first()
    if request.method == "GET":
        form = ClassesModelForm(instance=obj)  # 加上instance才能在编辑页面显示原来的数据
        return render(request, 'classes_edit.html', {"form": form})
    form = ClassesModelForm(data=request.POST, instance=obj)  # data是把编辑好的数据提交过去
    if form.is_valid():
        form.save()
        return redirect('classes_list')
    else:
        return render(request, 'classes_edit.html', {"form": form})


def classes_del(request, nid):
    """
    删除用户
    :param request:
    :param nid:
    :return:
    """
    models.ClassList.objects.filter(id=nid).delete()
    return redirect('classes_list')
