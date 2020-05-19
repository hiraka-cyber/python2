from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
def index(request):
    return render(request,'polls/index.html')

def detail(request):
    return render(request,'polls/detail.html')

def results(request):
    return render(request,'polls/results.html')

def good(request):
    return render(request,'polls/good.html')

def meet(request):
    return render(request,'polls/meet.html')

def beef(request):
    return render(request,'polls/beef.html')

def chicken(request):
    return render(request,'polls/chicken.html')

def fish(request):
    return render(request,'polls/fish.html')

def home(request):
    return render(request,'polls/home.html')

def all(request):
    return render(request,'polls/all.html')
