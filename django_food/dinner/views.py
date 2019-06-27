import json
from datetime import datetime, date
from decimal import Decimal

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import QuerySet
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from dinner.filters import DinnerFilter
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


def dinner_list(request):
    f = DinnerFilter(request.GET, queryset=DinnerInfo.objects.all())
    partion = Paginator(f.qs, 10)
    data = partion.get_page(request.GET.get('page', 1))
    return JsonResponse(request, 'active.html', {'filter': f, 'data': data})

class DinnerView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.__str__()
        elif isinstance(obj, Decimal):
            return obj.__str__()
        elif isinstance(obj, date):
            return obj.__str__()
        elif isinstance(obj, QuerySet):
            return list(obj)
        else:
            return json.JSONEncoder.default(self, obj)

class DinnerQuery(View):
    def get(self, request, *args, **kwargs):
        f = DinnerFilter(request.GET, queryset=DinnerInfo.objects.all())
        partion = Paginator(f.qs, 10)
        data = partion.get_page(request.GET.get('page', 1)).object_list.values()
        return JsonResponse({'data': data}, encoder=MyEncoder)

def dis_dinner(request):
    result = {
        'count': 0,
        'data': [],
        'total': 5,
        'page': 1
    }
    dinner_list=DinnerInfo.objects.all()
    total = int(request.GET.get('total', '5'))
    paginator = Paginator(dinner_list, total)
    page = request.GET.get('page',1)
    contacts = paginator.get_page(page)
    data_list=[]
    for obj in contacts:
        data=model_to_dict(obj)
        data['username'] = obj.user_id.username         # 用户名
        data['price']=obj.price                         # 饭局价格
        data['activities_play'] = obj.activities_play   # 活动玩法
        data['intro'] = obj.intro                       # 饭局简介
        data['dinnername'] = obj.dinner_title           # 饭局标题
        data['head'] = str(obj.user_id.head_image)      # 用户头像
        data['activities_photo'] = str(obj.activities_photo)# 活动照片
        data_list.append(data)
    result['count']=paginator.count/total
    result['data']=data_list
    result['page']=page
    #模型分页
    return JsonResponse({'result':result})

def my_dinner(request):
    my_dinner_list = DinnerInfo.objects.filter(user_id_id=request.user.id).values()
    my_dinner = dict(my_dinner_list)
    return JsonResponse({'my_dinner':my_dinner})















