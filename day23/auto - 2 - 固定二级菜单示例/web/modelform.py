from django.forms import ModelForm
from django import forms
from web import models


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = "__all__"
        error_messages = {  # 设置每个字段的报错提示信息
            "name": {
                "required": "订单名字不能为空"
            },
        }
