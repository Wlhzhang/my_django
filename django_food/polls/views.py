from django.contrib import auth
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from polls.cache_img import get_cache_code_info
from polls.forms import MyUserForm, LoginForm
from polls.models import MyUser

# 验证码
def get_code(request):
    img,code = get_cache_code_info()
    request.session['code'] = code
    return HttpResponse(img.getvalue(),content_type='image/png')

class Login(View):
    def get(self,request,*args,**kwargs):
        return render(request,'polls/login.html')
    def post(self,request,*args,**kwargs):
        form = LoginForm(request.POST)
        if request.session['code'] == request.POST.get('cache_code',None):
            if form.is_valid():
                user = auth.authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
                if user:
                    auth.login(request,user)
                    return JsonResponse({'status': 'success'})
                else:
                    return JsonResponse({'status': 'fail', 'msg': '账号或密码错误'})
            else:
                return JsonResponse({'status': 'fail', 'msg': '格式输入错误'})
        else:
            return JsonResponse({'status':'fail','msg':'验证码错误'})




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

class FindPassword(View):
    def get(self,request,*args,**kwargs):
        return render(request,'polls/forgot.html')
    def post(self,request,*args,**kwargs):
        user = MyUser.objects.all()
        find_email = request.POST.get('')



