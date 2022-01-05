from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    return render(request, 'hello.html', { 'name': 'Mosh'})

def say_main(request):
    return render(request, 'main.html')

def say_calculator(request):
    return render(request, 'calculator.html')

def say_basicmath(request):
    return render(request, 'basicmath.html')