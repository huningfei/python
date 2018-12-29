from django.forms import ModelForm
from web.forms.base import BootStrapModelForm
from web import models

class UserModelForm(BootStrapModelForm):
    class Meta:
        model = models.UserInfo
        fields = "__all__"