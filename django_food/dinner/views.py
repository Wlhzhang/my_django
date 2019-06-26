from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from dinner.forms import DinnerInfoForm
from dinner.models import DinnerInfo


def join_dinner(request):
    return render(request,'dining_center/Dinner.html')

def management(request):
    return render(request,'dining_center/Management.html')

class Release(View):
    def get(self,request,*args,**kwargs):
        return render(request,'dining_center/Release.html')
    def post(self,request,*args,**kwargs):
        dinner_form = DinnerInfoForm(request.POST,request.FILES)
        if dinner_form.is_valid():
            form_file = DinnerInfo(**dinner_form.cleaned_data)
            form_file.user_id=request.user
            form_file.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status':'fail','msg':'输入有误'})

def sing_up(request):
    return render(request,'dining_center/Sign_up.html')

def sing_success(request):
    return render(request,'dining_center/Success.html')