from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'polls/login.html')

def register(request):
    return render(request,'polls/reg.html')