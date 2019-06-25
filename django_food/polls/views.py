from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from polls.forms import MyUserForm
from polls.models import MyUser


def login(request):
    return render(request,'polls/login.html')

class Register(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'polls/register.html')
    def post(self,request,*args,**kwargs):
        form = MyUserForm(request.POST,request.FILES)
        if form.is_valid():
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 == password2:
                form_file = MyUser(
                    username = form.cleaned_data['username'],
                    email = form.cleaned_data['email']
                )
                form_file.set_password(password1)
                form_file.save()
                return JsonResponse({'status':'success'})
            else:
                return JsonResponse({'status':'password_fail','msg':'两次密码输入不一致'})
        else:
            return JsonResponse({'status':'form_error','msg':'验证格式失败'})

def forget_password(request):
    return render(request, 'polls/forget_password.html')

def find_password(request):
    return render(request,'polls/forgot.html')


