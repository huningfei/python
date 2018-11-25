from django.shortcuts import render, redirect, HttpResponse
from crm import models
from crm.forms.record import RecordModelForm
from django.urls import reverse


def record_list(request, nid):
    """
    跟进记录
    :param nid: 客户ID
    :param request:
    :return:
    """
    current_user_id = request.session['user_info']['id']  # 当前登录用户id
    # 查看该客户是否属于当前登录用户的私户，如果不是无权查看

    exists = models.Customer.objects.filter(id=nid, consultant_id=current_user_id).exists()
    if not exists:
        return HttpResponse('只能查看自己客户的跟进记录')
    queryset = models.ConsultRecord.objects.filter(customer_id=nid)

    return render(request, 'record_list.html', {'queryset': queryset, 'cid': nid})


def record_add(request, cid):
    """
    :param request:
    :param cid:
    :return:
    """
    if request.method == 'GET':
        form = RecordModelForm()
        return render(request, 'record_add.html', {'form': form})
    form = RecordModelForm(data=request.POST)
    if form.is_valid():
        # 添加的时候需要把客户id和当前登录用户的id都同时提交
        form.instance.customer_id = cid  # 客户id
        form.instance.consultant_id = request.session['user_info']['id']  # 当前登录id
        form.save()
        return redirect(reverse('record_list', args=(cid,)))
    return render(request, 'record_list.html', {'form': form})
