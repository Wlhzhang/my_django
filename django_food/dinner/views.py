import json
import math
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
from person.forms import SingForm
from person.models import SingDinner


def join_dinner(request):
    return render(request,'dining_center/Dinner.html')

def management(request):
    return render(request,'dining_center/Management.html')

# 发布自己的饭局
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

# 饭局报名
class SingUp(View):
    def get(self,request,*args,**kwargs):
        id = request.GET.get('id')
        print(id)
        return render(request,'dining_center/Sign_up.html',context=id)
    def post(self,request,*args,**kwargs):
        sing_forms = SingForm(request.POST,request.FILES)
        if sing_forms.is_valid():
            sing_file = SingDinner(
                dinner = request.GET.get('id'),
                apply_reason = sing_forms.cleaned_data['apply_reason'],
                remark = sing_forms.cleaned_data['remark']
            )
            print(request.user)
            sing_file.sing_user = request.user
            sing_file.save()
            return JsonResponse({'status':'success'})
        else:
            return JsonResponse({'status':'fail','msg':'请输入以上内容'})

# 报名成功
def sing_success(request):
    return render(request,'dining_center/Success.html')

#
# def dinner_list(request):
#     f = DinnerFilter(request.GET, queryset=DinnerInfo.objects.all())
#     partion = Paginator(f.qs, 10)
#     data = partion.get_page(request.GET.get('page', 1))
#     return JsonResponse(request, 'active.html', {'filter': f, 'data': data})
#
# class DinnerView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'index.html')

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
        info = [data['activities_play'],data['price__gte'],data['price__lte'],data['number__gte'],data['number__lte']]# 前端返回数的搜索表单的数据
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
    my_dinner = dict(my_dinner_list)
    return JsonResponse({'my_dinner':my_dinner})















