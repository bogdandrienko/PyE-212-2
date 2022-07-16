from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import datetime
import requests
import json
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    users = User.objects.all()  # все записи
    # users = User.objects.filter()  # все записи через массив условий
    # users = User.objects.order_by()  # все записи с сортивкой
    
    print(users)
    print(type(users))
    
    users_names = [x.username for x in users]
    print(users_names)
    print(type(users_names))
    print(users_names[0])
    print(type(users_names[0]))
    
    context = {"users_names": users_names, "count": len(users_names)}
    return render(request, "build/index.html", context=context)

def html(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def about(request):
    url = "https://jsonplaceholder.typicode.com/todos"
    headers = {
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }
    response = requests.get(
        url=url,
        headers=headers
    )
    
    # response.json()
    data = json.loads(response.content)
    
    return JsonResponse(data, safe=False)

def home(request):
    context = {}
    return render(request, "backend_api/home.html", context=context)

# HTTPresponse
# JsonResponse
# Model View Template - Model View Controller

# "react": "^18.2.0",
# "react-dom": "^18.2.0",
# "typescript": "^4.7.4",
# "react-scripts": "5.0.1",
# "redux-devtools-extension": "^2.13.9",
# "react-redux": "^8.0.2",

# "react-router-dom": "^6.3.0",

# "axios": "^0.27.2",