from django.shortcuts import render
from django.http import HttpResponse


# тут только "логика" - функции для обработки и возврат данных


def index(request):
    # return HttpResponse("Это чистая индекс страница")
    context = {

    }
    return render(request, 'app_second/pages/index.html', context)


def home(request):
    context = {

    }
    return render(request, 'app_second/pages/home.html', context)


def login(request):
    context = {

    }
    return render(request, 'app_second/pages/login.html', context)


def about(request):
    context = {

    }
    return render(request, 'app_second/pages/about.html', context)
