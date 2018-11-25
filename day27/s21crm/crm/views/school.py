from django.shortcuts import render, redirect
from crm import models
from crm.forms.school import SchoolModelForm
from django.urls import reverse


def school_list(request):
    """
    部门列表
    :param request:
    :return:
    """
    queryset = models.School.objects.all()
    return render(request, 'school_list.html', {'queryset': queryset})


def school_add(request):
    """
    部门添加
    :param request:
    :return:
    """

    if request.method == "GET":
        form = SchoolModelForm()
        return render(request, 'school_add.html', {'form': form})

    form = SchoolModelForm(data=request.POST)
    if form.is_valid():
        form.save()

        return redirect('school_list')
    else:
        return render(request, 'school_add.html', {'form': form})


def school_edit(request, nid):
    """
    编辑部门
    :param request:
    :param nid:
    :return:
    """
    obj = models.School.objects.filter(id=nid).first()
    if request.method == "GET":
        form = SchoolModelForm(instance=obj)  # 加上instance才能在编辑页面显示原来的数据
        return render(request, 'school_edit.html', {"form": form})
    form = SchoolModelForm(data=request.POST, instance=obj)  # data是把编辑好的数据提交过去
    if form.is_valid():
        form.save()
        return redirect('school_list')
    else:
        return render(request, 'school_edit.html', {"form": form})


def school_del(request, nid):
    """
    删除用户
    :param request:
    :param nid:
    :return:
    """
    models.School.objects.filter(id=nid).delete()
    return redirect('school_list')
