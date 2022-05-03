from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Это чистая индекс страница")

def home(request):
    context = {
        
    }
    return render(request, 'app_second/home.html', context)

def about(request):
    context = {
        
    }
    return render(request, 'app_second/about.html', context)


    