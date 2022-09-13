from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status


def index(request):
    context = {}
    return render(request=request, template_name='index.html', context=context, status=status.HTTP_200_OK)


def get_users(request):
    users = [{"id": x.id, "username": x.username, "email": x.email} for x in User.objects.all()]
    return JsonResponse(data=users, safe=False)
