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

# 登录
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
                return JsonResponse({'msg': '验证格式失败', 'status': 'form_error'})
        else:
            return JsonResponse({'status':'fail','msg':'验证码错误'})

# 退出登录
def logout(request):
    auth.logout(request)  #这一步就相当于直接session.flush()
    return redirect('/')

# 注册
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
            forms_error = form.errors.as_json()
            return JsonResponse({'msg': '验证格式失败', 'data': forms_error, 'status': 'form_error'})
            # return JsonResponse({'status':'form_error','msg':'验证格式失败'})

# 通过邮箱找回密码
class FindPassword(View):
    def get(self,request,*args,**kwargs):
        return render(request,'polls/forgot.html')
    def post(self,request,*args,**kwargs):
        find_email = request.POST.get('find_password_mail') # 接收前端返回的数据

        if find_email != None:# 如果输入邮箱为空，提示输入错误
            # 取出数据库与输入邮箱相匹配的用户信息
            user_info = MyUser.objects.filter(email=find_email)
            # 如果用户信息为空，提示该邮箱未注册
            print(user_info.values())
            if user_info != None:
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'fail', 'msg': '该邮箱未注册'})
        else:
            return JsonResponse({'status': 'fail', 'msg': '输入不能为空'})

# 我的饭局首页分页
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



