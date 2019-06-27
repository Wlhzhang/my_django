
from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.views import View

from person.forms import MyUserModifyForm
from polls.models import MyUser


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

def message(request):
    return render(request,'personal_center/Message.html')

def my_messages(request):
    return render(request,'personal_center/My_Messages.html')

def verified_bind_done(request):
    return render(request,'personal_center/Verified-bind-done.html')