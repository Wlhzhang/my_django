from django.contrib import auth
from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.views import View

from person.forms import MyUserModifyForm
from polls.models import MyUser

# 添加个人资料
class GetMen(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'personal_center/men.html')

    def post(self, request, *args, **kwargs):

        # user = get_object_or_404(MyUser, pk=request.user.id)
        # user_profile = get_object_or_404(MyUser, user=user)

        forms = MyUserModifyForm(request.POST,request.FILES)
        user = MyUser.objects.get(id=request.user.id)
        if forms.is_valid():
            # MyUser.objects.filter(id=request.user.id)
            # forms.user = request.user
            # form_file = user(**forms.cleaned_data)
            user.head_image = forms.cleaned_data['head_image']
            user.address = forms.cleaned_data['address']
            user.head_image = forms.cleaned_data['head_image']
            user.intro = forms.cleaned_data['intro']
            user.career = forms.cleaned_data['career']
            user.save()
            return JsonResponse({'status':'success'})
        else:
            return JsonResponse({'status':'fail','msg':'格式输入错误'})

def applyhost(request):
    return render(request,'personal_center/applyhost.html')

def detail(request):
    return render(request,'personal_center/detail.html')

# 修改密码
class ModifyPassword(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'personal_center/pwd.html')
    def post(self,request,*args,**kwargs):
        # 获取原密码
        password = request.POST.get('original_password')
        # 获取新密码
        password1 = request.POST.get('new_password')
        # 获取新密码确认
        password2 = request.POST.get('confirm_password')
        # 因为注册存密码时进行加密处理了，所以这里不能直接比较输入框的密码是否正确，需要用到check_password
        if request.user.check_password(password):
            if password1 != None:
                if password1 == password2:
                    user = request.user
                    user.set_password(password1)
                    user.save()
                    return JsonResponse({'status': 'success'})
                else:
                    return JsonResponse({'status': 'fail_one', 'msg': '两次密码输入不一致'})
            else:
                return JsonResponse({'status': 'fail_two', 'msg': '密码不能为空'})
        else:
            return JsonResponse({'status':'fail_two','msg':'原密码错误'})