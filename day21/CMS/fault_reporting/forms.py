from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from fault_reporting import models
import re


# 1. 正则的校验规则
# 2. 自定义函数
def check_email(value):  # 1@1.com
    ret = re.match(r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$', value)
    if not ret:
        # 邮箱格式匹配不上
        raise ValidationError("邮箱格式不正确")
    else:
        return value


# 注册的form类
class RegisterForm(forms.Form):

    username = forms.CharField(min_length=2, label="用户名")
    password = forms.CharField(
        label="密码",
        min_length=6,
        widget=forms.widgets.PasswordInput()
    )
    re_password = forms.CharField(
        label="确认密码",
        min_length=6,
        widget=forms.widgets.PasswordInput(attrs={"class": "form-control"})
    )
    phone = forms.CharField(
        label="手机号",
        min_length=11,
        max_length=11,
        validators=[RegexValidator(r'^1[3-9]\d{9}$', "手机号码格式不正确")],
    )
    email = forms.CharField(
        label="邮箱",
        validators=[check_email, ]
    )
     # 局部钩子
    def clean_username(self):
        # 做用户名不能重复的校验
        username = self.cleaned_data.get("username") #获取用户名
        # 去数据库查重
        is_exist = models.UserInfo.objects.filter(username=username)
        if is_exist:
            # 用户名已经被注册
            raise ValidationError("用户名已被注册")
        else:
            return username

    # 全局钩子，用来多多字段的比较
    def clean(self):
        pwd = self.cleaned_data.get("password")
        re_pwd = self.cleaned_data.get("re_password")

        if re_pwd != pwd:
            # 两次填写的密码不一致
            self.add_error("re_password", "两次密码不一致")
            raise ValidationError("两次密码不一致")
        else:
            return self.cleaned_data
     # 重写init
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        # 循环给每个字段加 class: form-control
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

