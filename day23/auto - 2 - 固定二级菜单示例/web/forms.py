from django import forms
from web import models


class UserForm(forms.Form):
    name = forms.CharField(
        max_length=12,
        min_length=2,
        # 如果想让网页显示中文就加上label
        label="用户名",
        error_messages={'required': '请输入用户名'},

        # 给tttle生成的input标签加上一个class类
        widget=forms.widgets.TextInput(attrs={"class": "form-control"})
    )
