from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#def index(request):
#    return HttpResponse("Hello, world. You're at the hello #index.")

def index(request):
    return render(request, 'hello/index.html')

def brian(request):
    return HttpResponse("Hello, Brian. You're at the hello index.")

def przemek(request):
    return HttpResponse("Hello, Przemek. You're at the hello index.")

def greet(request, name):
    return render(request, 'hello/greet.html', {'name': name.capitalize()})