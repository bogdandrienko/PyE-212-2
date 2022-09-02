import random
import time
import re

from django.contrib.auth.hashers import make_password
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
import datetime
import json
from django.contrib.auth.models import User, update_last_login
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.paginator import Paginator
from django.conf import settings

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from backend_api import models


# Create your views here.

def index(request):
    try:
        return render(request, "index.html", context={})
    except Exception as error:
        if settings.DEBUG:
            print(f"error {error}")
        return render(request, "components/404.html", context={})


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def registration(request):
    if request.method == "GET":
        return Response(data={"ответ:": r'(POST){"email": "admin@gmail.com", "password": "12345qwe!Brty"} '
                                        '=> <Response 201>'},
                        status=status.HTTP_200_OK)
    elif request.method == "POST":
        try:
            email = request.data.get("email", None)
            password = request.data.get("password", None)
            if email and password:
                if re.match(r"^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", password) and \
                        re.match(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", email):
                    User.objects.create(
                        username=email,
                        email=email,
                        password=make_password(password)  # для create НУЖНО шифровать пароль, для create_user НЕТ!
                    )
                    return Response(status=status.HTTP_201_CREATED)
                else:
                    return Response(data={"ответ:": "Вы не прошли проверку регулярного выражения"},
                                    status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response(data=str(error), status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
