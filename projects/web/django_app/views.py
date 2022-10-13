from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.


class HomeView(View):
    template_name = 'django_app/home.html'

    def get(self, request, *args, **kwargs):
        context = {
            "todos": [{"id": x, "title": f"title ({x})", "value": 18.978 * x} for x in range(1, 100)],
        }
        return render(request=request, template_name='django_app/home.html', context=context)

def home(request):
    context = {
        "todos": [{"id": x, "title": f"title ({x})", "value": 18.978 * x} for x in range(1, 100)],
    }
    return render(request=request, template_name='django_app/home.html', context=context)


def login(request):
    context = {
    }
    return render(request=request, template_name='django_app/home.html', context=context)
