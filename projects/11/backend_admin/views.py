import datetime
import time

from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render
import openpyxl
import os


# Create your views here.

def index(request):
    return render(request, 'backend_admin/AllLogs.html', context={})


def get_active_user_list(request):  # функция-контроллер
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
        "user_list": users,
        "excel_file": path
    }
    return render(request, 'backend_admin/GetUserList.html', context=context)

# класс-контроллер
