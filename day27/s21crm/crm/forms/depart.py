from django import forms
from crm import models


class DepartModelForm(forms.ModelForm):
    class Meta:
        model = models.Department  # 这里前面的model一定不要写models
        fields = '__all__'
        error_messages = {
            'title': {'required': '部门不能为空'}
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }
