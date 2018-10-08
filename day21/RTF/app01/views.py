from django.shortcuts import render,HttpResponse
import os
from django.http import JsonResponse  # json格式
# Create your views here.
# 富文本编辑器上传图片的视图
def upload_img(request):
    print(request.FILES)
    res = {"error": 0} # 这是固定写法，必须用error
    file_obj = request.FILES.get("imgFile")
    file_path = os.path.join("upload", "report_images", file_obj.name)

    # 将文件保存在本地
    with open(file_path, "wb") as f:
        for chunk in file_obj.chunks():
            f.write(chunk)
    # 将上传文件的url返回给富文本编辑器
    res["url"] = "/media/report_images/{}".format(file_obj.name)
    return JsonResponse(res)


def index(request):
    return render(request, "index.html", locals())