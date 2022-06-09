from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.models import User

# Create your views here.
from django.urls import reverse


def home(request):
    if request.user.is_authenticated is False:
        return redirect(reverse('login', args=()))
    return HttpResponse("<h1>HOME PAGE</h1>")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        print(f'username: {username}')
        print(f'password: {password}')

        user = authenticate(username=username, password=password)
        if user:
            django_login(request, user)
            print("success")
        else:
            print("fail")
    context = {}
    return render(request, 'app_teacher/pages/login.html', context)


def register(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        password2 = request.POST.get("password2", "")
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")
        email = request.POST.get("email", "")

        success = True
        # if not username or not password:
        if username == "" or password == "":
            print("имя пользователя или пароль пустые!")
            success = False

        if password != password2:
            print("пароли не совпадают!")
            success = False

        user = User.objects.get(username=username)
        if user:
            print("пользователь уже существует!")
            success = False

        if success:
            # 1 способ
            obj = User.objects.create(
                username=username,
                password=make_password(password),
                first_name=first_name,
                last_name=last_name,
                email=email,
                
            )
            obj.save()

            # 2 способ
            # obj = User.objects.create(
            #     username=username,
            #     first_name=username,
            #     last_name=username,
            #     email=username,
            # )
            # obj.set_password(password)
            # obj.save()
    context = {}
    return render(request, 'app_teacher/pages/register.html', context)
