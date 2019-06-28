import math

from django.contrib import auth
from django.core.paginator import Paginator
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from dinner.models import DinnerInfo
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
                user = auth.authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password']) # 自动给你的user表自动校验
                if user:
                    auth.login(request,user)
                    return JsonResponse({'status': 'success'})
                else:
                    return JsonResponse({'status': 'fail', 'msg': '账号或密码错误'})
            else:
                return JsonResponse({'status': 'fail', 'msg': '格式输入错误'})
        else:
            return JsonResponse({'status':'fail','msg':'验证码错误'})

# 退出登录
def logout(request):
    auth.logout(request)  #这一步就相当于直接session.flush()
    return redirect('/')

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
        find_email = request.POST.get('find_password_mail')
        # if MyUser.email == find_email:
        #     id = MyUser.

        print(find_email)
        return JsonResponse('000')

def dinner_home_fenye(request):
    result = {
        'count': 0,
        'data': [],
        'total': 5,
        'page': 1
    }
    data = request.GET
    print(data)
    dinner_list = DinnerInfo.objects.all()
    total = int(request.GET.get('total', '5'))
    paginator = Paginator(dinner_list, total)
    page = request.GET.get('page', 1)
    contacts = paginator.get_page(page)
    data_list = []
    for obj in contacts:
        data = model_to_dict(obj)
        data['username'] = obj.user_id.username  # 用户名
        data['price'] = obj.price  # 饭局价格
        data['activities_play'] = obj.activities_play  # 活动玩法
        data['intro'] = obj.intro  # 饭局简介
        data['dinnername'] = obj.dinner_title  # 饭局标题
        data['head'] = str(obj.user_id.head_image)  # 用户头像
        data['activities_photo'] = str(obj.activities_photo)  # 活动照片
        data_list.append(data)
    result['count'] = math.ceil(paginator.count / total)
    result['data'] = data_list
    result['page'] = page
    # 模型分页
    return JsonResponse({'result': result})



