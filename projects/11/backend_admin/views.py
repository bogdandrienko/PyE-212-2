from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'backend_admin/AllLogs.html', context={})
