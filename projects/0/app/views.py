from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import models


# Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at the polls home.")


def index(request):
    latest_question_list = models.Todo.objects.order_by('-updated')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'app/index.html', context)
