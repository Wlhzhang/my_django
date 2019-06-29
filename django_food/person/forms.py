from django import forms

from person.models import SingDinner
from polls.models import MyUser


class MyUserModifyForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = (
            'head_image','sex','career','address','intro'
        )

class SingForm(forms.ModelForm):
    class Meta:
        model = SingDinner
        fields = (
            'apply_reason','remark'
        )
