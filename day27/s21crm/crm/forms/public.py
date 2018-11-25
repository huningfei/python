from django import forms
from crm import models
from crm.pwd.md5 import md5

# import md5
class PublicCustomModelForm(forms.ModelForm):
    class Meta:
        model = models.Customer # 这里前面的model一定不要写models
        # fields = '__all__'
        exclude=['consultant','status']

    def __init__(self, *args, **kwargs):
        # 在父类的初始化方法中将7个字段当成字典放到了 self.fields 中。
        super(PublicCustomModelForm, self).__init__(*args, **kwargs)

        for key, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

