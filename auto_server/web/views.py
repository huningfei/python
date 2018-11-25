from django.shortcuts import render
from repository import models
from django.http import JsonResponse


def server(request):
    return render(request, 'server.html')


# Create your views here.
def server_json(request):
    table_config = [
        {
            'q': 'hostname',
            'title': '主机名',

        },
        {
            'q': 'sn',
            'title': '序列号',

        },
        {
            'q': 'os_platform',
            'title': '系统',

        },
    ]
    values = []
    for item in table_config:
        values.append(item['q'])
    server_list = models.Server.objects.values(*values)
    print(server_list)
    response = {
        'data_list': list(server_list),
        'table_config': table_config
    }
    return JsonResponse(response)
