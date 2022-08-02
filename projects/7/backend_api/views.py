import time

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
import datetime
import requests
import json
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from backend_api import models
from backend_api import serializers


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


from django.views.decorators.csrf import csrf_exempt


# @api_view(http_method_names=["GET", "POST"])
# @permission_classes([AllowAny])
@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        if username and password:
            return JsonResponse({"response": "Успешно вошли"}, safe=False)
        else:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=405)


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

    page = int(request.GET.get("page", 1))
    limit = int(request.GET.get("limit", 10))
    filter = str(request.GET.get("filter", ""))

    print(f"page: {page}")
    print(f"limit: {limit}")
    print(f"filter: {filter}")

    data = json.loads(response.content)
    paginator_obj = Paginator(data, limit)
    current_page = paginator_obj.get_page(page).object_list

    res = {"current_page": current_page, "x-total-count": len(data)}

    print(f"current_page: {current_page}")

    # response.json()

    return JsonResponse(res, safe=False)


def home(request):
    context = {}
    return render(request, "backend_api/home.html", context=context)


@api_view(http_method_names=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"])
@permission_classes([AllowAny])
def news(request, book_id=0):

    time.sleep(3)

    if int(book_id) >= 1:
        if request.method == "GET":  # получение книги
            book = get_object_or_404(models.ModelBook, id=book_id)
            serialized_book = serializers.BookSerializer(instance=book, many=False).data
            return Response(data=serialized_book, status=status.HTTP_200_OK)
        elif request.method == "DELETE":
            book = models.ModelBook.objects.get(id=book_id).delete()
            book.delete()
            return Response(data={"response": "Успешно удалено."}, status=status.HTTP_200_OK)
        elif request.method == "PUT" or request.method == "PATCH":
            book = models.ModelBook.objects.get(id=book_id)

            title = request.POST.get("title", "Шаблон заголовка")
            description = request.POST.get("description", "Шаблон описания")
            if book.title != title:
                book.title = title
            if book.description != description:
                book.description = description
            book.save()

            book = models.ModelBook.objects.get(id=book_id)
            serialized_book = serializers.BookSerializer(instance=book, many=False).data
            return Response(data=serialized_book, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    else:
        if request.method == "GET":  # получение книг
            books = models.ModelBook.objects.all()  # order_by filter ...
            serialized_book = serializers.BookSerializer(instance=books, many=True).data
            return Response(data=serialized_book, status=status.HTTP_200_OK)
        elif request.method == "POST":  # создание книги
            title = request.POST.get("title", "Шаблон заголовка")
            description = request.POST.get("description", "Шаблон описания")
            models.ModelBook.objects.create(
                title=title,
                description=description
            )
            return Response(data={"response": "Успешно создано."}, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

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
