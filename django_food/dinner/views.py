import json
import math
from datetime import datetime, date
from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import QuerySet
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

import dinner
from dinner.filters import DinnerFilter
from dinner.forms import DinnerInfoForm
from dinner.models import DinnerInfo
from person.forms import SingForm
from person.models import SingDinner


def join_dinner(request):
    return render(request,'dining_center/Dinner.html')

# 报名的饭局信息
def sing_dinner(request):
    if request.method == 'GET':
        sing_infos = SingDinner.objects.filter(sing_user=request.user)
        data = []
        # dinner_info = DinnerInfo.objects.filter(id=sing_info.dinner_id)
        for sing_info in sing_infos:

            result = {'dinner_title':sing_info.dinner.dinner_title,
                    'price':sing_info.dinner.price,
                    'number':sing_info.dinner.number,
                    'activities_play':sing_info.dinner.activities_play,
                    'activities_photo':str(sing_info.dinner.activities_photo),
                    'intro':sing_info.dinner.intro}
            data.append(result)
        return JsonResponse({'data':data})

def management(request):
    return render(request,'dining_center/Management.html')


@login_required
# 发布自己的饭局
def release(request):
    if request.method == 'GET':
        return render(request,'dining_center/Release.html')
    if request.method == 'POST':
        try:
            dinner_form = DinnerInfoForm(request.POST,request.FILES)
            if dinner_form.is_valid():
                form_file = DinnerInfo(**dinner_form.cleaned_data)
                form_file.user_id=request.user
                form_file.save()
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status':'fail','msg':'输入有误'})
        except:
            return render(request,'polls/login.html')


# 饭局报名
class SingUp(View):
    def get(self,request,*args,**kwargs):
        # print(id)
        global id
        id = request.GET.get('id')
        return render(request,'dining_center/Sign_up.html',context={'id':id})
    def post(self,request,*args,**kwargs):
        sing_forms = SingForm(request.POST)
        # dinner_id = SingDinner.objects.get(dinner=ac_id)
        # print(dinner_id)
        if sing_forms.is_valid():
            sing_file = SingDinner(
                # 这里存dinner的关联时要用instance对象，不然报错ValueError: Cannot assign "''": "SingDinner.dinner" must be a "DinnerInfo" instance.
                dinner = DinnerInfo.objects.filter(id=id).first(),
                apply_reason = sing_forms.cleaned_data['apply_reason'],
                remark = sing_forms.cleaned_data['remark']
            )
            sing_file.sing_user= request.user
            sing_file.save()
            return JsonResponse({'status':'success'})
        else:
            return JsonResponse({'status':'fail','msg':'请输入以上内容'})

# 报名成功
def sing_success(request):
    return render(request,'dining_center/Success.html')

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

# 分页查询
class DisDinner(View):

    def fenye(self,contacts,paginator,page,total):
        result = {
            'count': 0,
            'data': [],
            'total': 5,
            'page': 1
        }
        data_list = []
        for obj in contacts:
            data = model_to_dict(obj)
            data['id'] = obj.id
            data['number'] = obj.number
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
        return result

    def get(self,request,*args,**kwargs):
        data = request.GET # 接收前端数据
        info = [data['price__gte'],data['price__lte'],data['number__gte'],data['number__lte']]# 前端返回数的搜索表单的数据
        # 如果info为空，执行分页，不为空执行查询分页
        if info != None:
            # 查询分页
            f = DinnerFilter(request.GET, queryset=DinnerInfo.objects.all())
            total = int(request.GET.get('total', '5')) # 每页显示数据条数
            paginator = Paginator(f.qs, total)
            page = request.GET.get('page', 1)          # 获取前端当前页码
            contacts = paginator.get_page(page)        # 对应前端页码的所在页数据
            result = self.fenye(contacts,paginator,page,total)
            return JsonResponse({'result': result}, encoder=MyEncoder)
        else:
            # 分页
            dinner_list=DinnerInfo.objects.all()
            total = int(request.GET.get('total', '5'))
            print(total)
            paginator = Paginator(dinner_list, total)
            page = request.GET.get('page',1)
            contacts = paginator.get_page(page)
            result = self.fenye(contacts,paginator,page,total)
            #模型分页
            return JsonResponse({'result':result})

# 用户自己发布的饭局
def my_dinner(request):
    my_dinner_list = DinnerInfo.objects.filter(user_id_id=request.user.id).values()
    my_dinner = list(my_dinner_list)
    return JsonResponse({'my_dinner':my_dinner})















