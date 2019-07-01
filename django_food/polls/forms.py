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
            raise forms.ValidationError('用户名格式不正确')
        return self.cleaned_data["username"]

    def clean_my_file(self):
        return self.cleaned_data['head_image']


class LoginForm(forms.Form):
        username = forms.CharField(max_length=30, min_length=4, required=True,
                                   error_messages={'max_length': '用户名最大长度超出8个字符',
                                                   'min_length': '用户名最小长度至少为4个字符', })
        password = forms.CharField(max_length=30, min_length=5, required=True,
                                   error_messages={'max_length': '密码最大长度超出10个字符',
                                                   'min_length': '密码最小长度至少为5个字符'})
        def clean_username(self):
            regex=r'\w{4,8}'
            if re.findall(regex,self.cleaned_data["username"]) is None:
                raise forms.ValidationError('用户名格式不正确')
            return self.cleaned_data["username"]
        def clean_password(self):
            regex=r'\w{5,10}'
            if re.findall(regex,self.cleaned_data["password"]) is None:
                raise forms.ValidationError('密码格式不正确')
            return self.cleaned_data["password"]

class EmailForm(forms.Form):
    find_password_mail = forms.EmailField(label='验证邮箱')