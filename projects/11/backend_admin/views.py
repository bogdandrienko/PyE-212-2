import datetime
import time

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import openpyxl
import os

from django.urls import reverse
from django.views import View

from backend_admin import forms


def login_required(func):
    def wrap(*args, **kwargs):  # (admin, 12345qwerty,) {"username": 'admin', "password": '12345qwerty'}

        if not args[1].user.is_authenticated:
            return redirect(reverse('login', args=()))
        elif not args[1].user.is_superuser and not args[1].user.is_staff:
            return redirect(reverse('login', args=()))

        result = func(*args, **kwargs)
        return result

    return wrap


ACTION_LOGGING = True
ERROR_LOGGING = True


def loger(func):
    if ACTION_LOGGING:
        pass

    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrap


class HomeView(View):

    @loger
    @login_required
    def get(self, request):
        #
        # if not request.user.is_authenticated:
        #     return redirect(reverse('login', args=()))
        #

        return render(request, 'backend_admin/Home.html', context={})


# def home(request):
#     return render(request, 'backend_admin/Home.html', context={})


class GetActiveUserListView(View):
    initial = {'key': 'value'}
    template_name = 'backend_admin/GetUserList.html'

    @login_required
    def get(self, request, *args, **kwargs):
        users = User.objects.filter(is_active=True)  # только активные пользователи

        # EXCEL GENERATOR
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        kwargs_list = ["username", "password", "id", "is_superuser"]
        users_list = [x for x in users]  # list comprehension (pre generator yeld)
        for kwarg in kwargs_list:
            worksheet.cell(row=1, column=kwargs_list.index(kwarg) + 1, value=kwarg)
        for user_obj in users_list:
            row_index = users_list.index(user_obj)
            for kwarg in kwargs_list:
                col_index = kwargs_list.index(kwarg)
                worksheet.cell(row=row_index + 2, column=col_index + 1, value=getattr(user_obj, kwarg))
        path = f'temp/new_{datetime.datetime.now().strftime("%m-%d-%Y %H-%M-%S-%f")}.xlsx'
        directory = os.path.join("static", "temp")
        if not os.path.exists(directory):
            os.mkdir(directory)
        if os.path.exists(settings.STATIC_URL[1:] + path):
            os.remove(settings.STATIC_URL[1:] + path)
        workbook.save(settings.STATIC_URL[1:] + path)
        # EXCEL GENERATOR

        context = {
            "title": "Абракадабра",
            "headers": ["id", "username", "password", "password", "password", "is_superuser"],
            "user_list": users,
            "excel_file": path
        }

        return render(request, self.template_name, context)


@login_required
def get_active_user_list(request):  # функция-контроллер
    try:

        if not request.user.is_authenticated:
            return redirect(reverse('login', args=()))

        users = User.objects.filter(is_active=True)  # только активные пользователи

        # EXCEL GENERATOR
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        kwargs_list = ["username", "password", "id", "is_superuser"]
        users_list = [x for x in users]  # list comprehension (pre generator yeld)
        for kwarg in kwargs_list:
            worksheet.cell(row=1, column=kwargs_list.index(kwarg) + 1, value=kwarg)
        for user_obj in users_list:
            row_index = users_list.index(user_obj)
            for kwarg in kwargs_list:
                col_index = kwargs_list.index(kwarg)
                worksheet.cell(row=row_index + 2, column=col_index + 1, value=getattr(user_obj, kwarg))
        path = f'temp/new_{datetime.datetime.now().strftime("%m-%d-%Y %H-%M-%S-%f")}.xlsx'
        directory = os.path.join("static", "temp")
        if not os.path.exists(directory):
            os.mkdir(directory)
        if os.path.exists(settings.STATIC_URL[1:] + path):
            os.remove(settings.STATIC_URL[1:] + path)
        workbook.save(settings.STATIC_URL[1:] + path)
        # EXCEL GENERATOR

        context = {
            "title": "Абракадабра",
            "headers": ["id", "username", "password", "password", "password", "is_superuser"],
            "user_list": users,
            "excel_file": path
        }
        return render(request, 'backend_admin/GetUserList.html', context=context)
    except Exception as error:
        if settings.DEBUG:
            print(f"error {error}")
        return render(request, "components/404.html", context={})


def django_login(request):
    try:
        if request.method == "GET":
            context = {
                "login_form": forms.LoginUserForm()
            }
            return render(request, "backend_admin/Login.html", context=context)
        if request.method == "POST":

            print(request.POST)

            email = request.POST["email"]
            password = request.POST["password"]
            if email and password:
                user = authenticate(username=email, password=password)
                if user:
                    login(request, user)
                    return redirect(reverse('home', args=()))
            return redirect(reverse('login', args=()))
    except Exception as error:
        if settings.DEBUG:
            print(f"error {error}")
        return render(request, "components/404.html", context={})


def django_logout(request):
    try:
        logout(request)
        return redirect(reverse('login', args=()))
    except Exception as error:
        if settings.DEBUG:
            print(f"error {error}")
        return render(request, "components/404.html", context={})
