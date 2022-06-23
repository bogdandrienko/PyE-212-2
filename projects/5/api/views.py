from django.shortcuts import render


# Create your views here.

def home(request):
    context = {}
    return render(request, 'build/index.html', context)


def test(request):
    context = {}
    return render(request, 'public/index.html', context)
