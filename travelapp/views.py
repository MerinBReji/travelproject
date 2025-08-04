from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import place



# Create your views here.
def fun(request):
    obj=place()
    obj.name="Kerala"
    obj.price=100
    obj.desc="This is kerala"
    return render(request,"index.html",{'result':obj})

def add(request):
    num1=int(request.POST["num1"])
    num2=int(request.POST["num2"])
    num3=num1+num2
    return render(request,"result.html",{"add":num3})