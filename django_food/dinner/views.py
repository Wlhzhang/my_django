from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.forms import model_to_dict
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

def dis_dinner(request):

    # course_list = DinnerInfo.objects.all()
    # # 生成pagintor对象，定义每页显示10条记录
    # paginator = Paginator(course_list, 10)
    #
    # # 获取当前的页码数，默认为1
    # page = request.GET.get("page", 1)
    #
    # # 把当前的页码数转换为整数类型
    # currentPage = int(page)
    #
    # try:
    #     video_list = paginator.page(page)  # 获取当前页码的记录
    # except PageNotAnInteger:
    #     video_list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    # except EmptyPage:
    #     video_list = paginator.page(paginator.num_pages)  # 如果用户输入的页码不是整数时,显示第1页的内容
    #
    # # return render(request, "ceshi.html", locals())
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
        username = obj.dinner_title
        price = obj.price
        activities_play = obj.activities_play
        intro = obj.intro
        executor_list=[]
        for executor in obj.user_id.all():
            name = executor.username
            head = executor.head_image
            executor_list.append(name)
            executor_list.append(head)
        data=model_to_dict(obj)
        data['user'] = username
        data['price']=price
        data['activities_play'] = activities_play
        data['intro'] = intro
        data['executor']=executor_list
        data_list.append(data)
    result['count']=paginator.count/total
    result['data']=data_list
    result['page']=page
    #模型分页
    return JsonResponse({'result':result})

















