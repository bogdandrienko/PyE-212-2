import random
import time
import re

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
    return render(request, 'index.html', context={})


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def registration(request):
    if request.method == "POST":
        email = request.data.get("email", None)
        password = request.data.get("password", None)

        print(f"\nGET {request.GET}")
        print(f"POST {request.POST}")
        print(f"data {request.data}")
        print(f"FILES {request.FILES}\n")

        print(email)
        print(password)

        if email and password:
            if re.match(r"^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", password) and \
                    re.match(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", email):
                User.objects.create_user(
                    username=email,
                    email=email,
                    password=password
                )

                # {
                #     "email": "admin@gmail.com",
                #     "password": "adminA1#"
                # }
                pass
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(data={"ответ:": "Вы не прошли проверку регулярного выражения"}, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
