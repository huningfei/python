from django import forms
from crm import models


class SchoolModelForm(forms.ModelForm):
    class Meta:
        model = models.School  # 这里前面的model一定不要写models
        fields = '__all__'
        error_messages = {
            'title': {'required': '学校不能为空'}
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }
