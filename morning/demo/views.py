from django.shortcuts import render
from django.http import HttpResponse
from .models import Demo
# Create your views here.

# def one(request):
#     return HttpResponse("Hello")

# def two(request):
#     return HttpResponse("<h1>Welcome</h1>")

# def three(request):
#     v = "mani"
#     return render(request,"one.html")

# def four(request):
#     return HttpResponse("<h1>Welcome</h1>")

def html(request):
    return render(request,"one.html")

def html1(request):
    if request.method == "POST":
        name = request.POST["name"]
        password = request.POST["password"]
        obj = Demo()
        obj.name = name
        obj.password = password
        obj.save()
    return render(request,"two.html",{'name':name,'password':password})