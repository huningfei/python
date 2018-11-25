from django import forms
from crm import models


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = models.Course  # 这里前面的model一定不要写models
        fields = '__all__'
        error_messages = {
            'name': {'required': '课程不能为空'}
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }
