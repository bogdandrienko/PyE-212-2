from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    context = {}
    return render(request, 'build/index.html', context)


def test(request):
    context = {}
    return render(request, 'public/index.html', context)


def get_users_count(request):
    users = User.objects.all().count()
    return JsonResponse({"users": users})
