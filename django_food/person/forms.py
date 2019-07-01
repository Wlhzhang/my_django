from django import forms

from person.models import SingDinner
from polls.models import MyUser


class MyUserModifyForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = (
            'head_image','sex','career','intro'
        )
    province = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    zone = forms.CharField(max_length=50)

class SingForm(forms.ModelForm):
    class Meta:
        model = SingDinner
        fields = (
            'apply_reason','remark'
        )
