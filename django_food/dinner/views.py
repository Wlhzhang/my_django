from django.shortcuts import render

# Create your views here.
def join_dinner(request):
    return render(request,'dining_center/Dinner.html')

def management(request):
    return render(request,'dining_center/Management.html')

def release(request):
    return render(request,'dining_center/Release.html')

def sing_up(request):
    return render(request,'dining_center/Sign_up.html')

def sing_success(request):
    return render(request,'dining_center/Success.html')