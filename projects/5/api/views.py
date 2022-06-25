from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response

from . import serializers

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def home(request):
    context = {}
    return render(request, 'build/index.html', context)


def test(request):
    context = {}
    return render(request, 'public/index.html', context)


def get_users(request):
    users = User.objects.all()
    print(type(users))
    print(users)
    serialized_users = serializers.UserSerializer(instance=users, many=True).data
    print(type(serialized_users))
    print(serialized_users)
    # return JsonResponse({"users": serialized_users})
    return Response(serialized_users)


def get_users_count(request):
    users = User.objects.all().count()
    return JsonResponse({"users": users})


@csrf_exempt
def create_user(request):
    # логика создания пользователя

    # print(f"request : {request}")
    # print(f"request.POST : {request.POST}")

    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    print(f"username == {username}")
    print(f"password == {password}")

    User.objects.create(
        username=username,
        password=password,
        email=""
    )

    value = True

    # логика создания пользователя
    return JsonResponse({"result": "Пользователь успешно создан!"})
