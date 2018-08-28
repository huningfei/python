from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from app01 import models

class BookModelForm(forms.ModelForm):
    class Meta:
        model=models.Book
        fields="__all__" #model类里面所有的字段都展示
        # fields="title" # 指定展示某些字段
        # exclude=["title"] # 除了知道字段，其他字段都展示
        # labels可以设置在网页上面显示的文字
        labels={
            "title":"书名",
            "publisher_date":"创建日期",
            "phone":"手机号",
            "publisher":"出版社",
            "authors":"作者",

        }
        widgets={ # 设置每个字段的插件信息
            "title": forms.widgets.TextInput(attrs={"class": "form-control"}),
            "phone": forms.widgets.TextInput(attrs={"class": "form-control"}),
            "publisher": forms.widgets.Select(attrs={"class": "form-control"}),
            "authors": forms.widgets.SelectMultiple(attrs={"class": "form-control"}),

        }
        error_messages = {  # 设置每个字段的报错提示信息
            "publisher": {
                "required": "必须给我选一个出版社！"
            },
            "authors":{
                "required":"必须选择一个作者"

            }
        }