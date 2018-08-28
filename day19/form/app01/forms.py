from django import forms
from app01 import models
from django.core.exceptions import ValidationError #注册功能
from django.core.validators import RegexValidator # 检验手机号码是否正确

# 自己定义一个form类
class BookForm(forms.Form):
    title=forms.CharField(
        max_length=12,
        min_length=2,
        # 如果想让网页显示中文就加上label
        label="书名",
        initial="填写书名",
        # 给tttle生成的input标签加上一个class类
        widget=forms.widgets.TextInput(attrs={"class":"form-control"})
    )
    publisher_date=forms.DateField(
        label="出版日期",
        # widget 插件
        widget=forms.widgets.DateInput(attrs={"type":"date","class":"form-control"})
    )
    phone=forms.CharField(
        max_length=11,
        validators=[RegexValidator(r'^1[356789]\d{9}$',"手机号码格式不正确")],  # 限制手机号格式
        widget = forms.widgets.TextInput(attrs={"class": "form-control"})
    )
    # 用modelchoicefield可以实时显示到页面上面当数据库增加的时候
    publisher = forms.ModelChoiceField(
        queryset=models.Publisher.objects.all(),
        widget=forms.widgets.Select(attrs={"class": "form-control"}),
    )
    authors=forms.ModelMultipleChoiceField(
        queryset=models.Author.objects.all(),
        widget=forms.widgets.SelectMultiple(attrs={"class": "form-control"})
    )
    #自定义一个局部钩子函数含有alex的关键字不能提交
    def clean_title(self):
        value=self.cleaned_data.get("title")  #获取书名
        if "alex" in value:
            raise ValidationError("ALEX以备和谐")
        else:
            return value

