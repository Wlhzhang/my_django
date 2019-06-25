import re

from django import forms

from polls.models import MyUser


class MyUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = (
            'username','email'
        )
    password1 = forms.CharField(label='设置密码',max_length=20)
    password2 = forms.CharField(label='重复密码',max_length=20)

    def clean_username(self):
        regex = r'\w{4,8}'
        if re.findall(regex, self.cleaned_data["username"]) is None:
            raise forms.ValidationError('输入格式不正确')
        return self.cleaned_data["username"]

    def clean_my_file(self):
        return self.cleaned_data['head_image']