from django import forms
from crm import models
from crm.pwd.md5 import md5

# import md5
class UserInfoModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo  # 这里前面的model一定不要写models
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # 在父类的初始化方法中将7个字段当成字典放到了 self.fields 中。
        super(UserInfoModelForm, self).__init__(*args, **kwargs)

        for key, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_password(self):
        """
        密码对应的钩子方法
        :return:
        """
        user_input_pwd = self.cleaned_data['password']
        return md5(user_input_pwd)
