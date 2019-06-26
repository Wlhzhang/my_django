from django.shortcuts import render

# Create your views here.
def get_men(request):
    return render(request,'personal_center/mem.html')

def applyhost(request):
    return render(request,'personal_center/applyhost.html')

def detail(request):
    return render(request,'personal_center/detail.html')

def fans(request):
    return render(request,'personal_center/fans.html')

def main(request):
    return render(request,'personal_center/main.html')

def message(request):
    return render(request,'personal_center/Message.html')

def my_messages(request):
    return render(request,'personal_center/My_Messages.html')

def upfiles(request):
    return render(request,'personal_center/upfiles.html')

def verified_bind_done(request):
    return render(request,'personal_center/Verified-bind-done.html')