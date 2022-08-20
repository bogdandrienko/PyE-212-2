from django.shortcuts import render
from rest_framework import status


def index(request):
    context = {}
    return render(request=request, template_name='index.html', context=context, status=status.HTTP_200_OK)
