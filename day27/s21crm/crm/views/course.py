from django.shortcuts import render, redirect
from crm import models
from crm.forms.course import CourseModelForm
from django.urls import reverse


def course_list(request):
    """
    部门列表
    :param request:
    :return:
    """
    queryset = models.Course.objects.all()
    return render(request, 'course_list.html', {'queryset': queryset})


def course_add(request):
    """
    部门添加
    :param request:
    :return:
    """

    if request.method == "GET":
        form = CourseModelForm()
        return render(request, 'course_add.html', {'form': form})

    form = CourseModelForm(data=request.POST)
    if form.is_valid():
        form.save()

        return redirect('course_list')
    else:
        return render(request, 'course_add.html', {'form': form})


def course_edit(request, nid):
    """
    编辑部门
    :param request:
    :param nid:
    :return:
    """
    obj = models.Course.objects.filter(id=nid).first()
    if request.method == "GET":
        form = CourseModelForm(instance=obj)  # 加上instance才能在编辑页面显示原来的数据
        return render(request, 'course_edit.html', {"form": form})
    form = CourseModelForm(data=request.POST, instance=obj)  # data是把编辑好的数据提交过去
    if form.is_valid():
        form.save()
        return redirect('course_list')
    else:
        return render(request, 'course_edit.html', {"form": form})


def course_del(request, nid):
    """
    删除用户
    :param request:
    :param nid:
    :return:
    """
    models.Course.objects.filter(id=nid).delete()
    return redirect('course_list')
