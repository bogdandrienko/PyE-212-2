import time

from django.core.paginator import Paginator
from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
import datetime
import requests
import json
from django.contrib.auth.models import User, update_last_login
from django.core.paginator import Paginator
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from backend_api import models
from backend_api import serializers


def index(request):
    # send_mail(
    #     'Проверка',
    #     'Проверка сообщения.',
    #     'eevee.cycle1@yandex.ru',
    #     ['bogdandrienko@gmail.com'],
    #     fail_silently=False,
    # )

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


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
# @csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        if username and password:
            user = User.objects.get(username=username)
            update_last_login(sender=None, user=user)
            refresh = RefreshToken.for_user(user=user)
            response = {"response": {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "token": str(refresh.access_token),
            }}
            return Response(response)
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
    time.sleep(2)

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

            from django.core.paginator import Paginator
            page = request.GET.get("page", 1)
            limit = request.GET.get("limit", 5)

            # search / filter / order_by
            books = models.ModelBook.objects.all()  # .filter().order_by()  # order_by filter ... # [1, 2, 3, 4, 5 ... 500]

            count = len(books)
            for i in books:
                print(i.return_clear_data())
            paginator_instanse = Paginator(books, limit)  # [1, 2, 3, 4, 5]
            books = paginator_instanse.get_page(number=page).object_list

            serialized_books = serializers.BookSerializer(instance=books, many=True).data
            return Response(data={"object_list": serialized_books, "count": count}, status=status.HTTP_200_OK)
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


@api_view(http_method_names=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"])
# @permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
# @csrf_exempt
def categories(request, book_id=0):
    print(request)

    print(str(request.auth))
    print(str(request.META.get("HTTP_AUTHORIZATION", "")))

    # token = str(request.META.get("HTTP_AUTHORIZATION", "Bearer $")).split("Bearer ")[1].strip()
    # print(f"token: {token}\n")
    # print(request.META.get("HTTP_AUTHORIZATION", "").replace("Basic ", ""))

    # for key, value in request.META.items():
    #     # print(key[:50], value[:50])
    #     pass

    time.sleep(2)

    # print(request.META['AUTHORIZATION'])
    # print(request.META['HTTP_AUTHORIZATION'])
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

            # return Response(status=status.HTTP_401_UNAUTHORIZED)

            from django.core.paginator import Paginator
            page = request.GET.get("page", 1)
            limit = request.GET.get("limit", 5)

            # search / filter / order_by
            categories_list = models.ModelBookCategory.objects.all()  # .filter().order_by()  # order_by filter ... # [1, 2, 3, 4, 5 ... 500]
            count = len(categories_list)
            paginator_instanse = Paginator(categories_list, limit)  # [1, 2, 3, 4, 5]
            categories_list = paginator_instanse.get_page(number=page).object_list

            serialized_categories = serializers.BookCategorySerializer(instance=categories_list, many=True).data

            # user = User.objects.get(username="admin")
            # update_last_login(sender=None, user=user)
            # refresh = RefreshToken.for_user(user=user)
            # response = {"response": {
            #     "refresh": str(refresh),
            #     "access": str(refresh.access_token),
            #     "token": str(refresh.access_token),
            # }}

            return Response(data={"object_list": serialized_categories, "count": count, "response": "response"},
                            status=status.HTTP_200_OK)
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


@api_view(http_method_names=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"])
# @permission_classes([AllowAny])  # Все пользователи
@permission_classes([IsAuthenticated])  # Только авторизованные пользователи
def get_data(request):
    # username = request.POST.get("username", None)
    # password = request.POST.get("password", None)
    # user = authenticate(username=username, password=password)
    # refresh = RefreshToken.for_user(user=user)
    # tokens = dict(refresh_token=str(refresh), access_token=str(refresh.access_token))
    # return Response(data=tokens, status=status.HTTP_200_OK)

    tokens = {}

    # print(str(request.META.get("HTTP_AUTHORIZATION", "")))
    # token = str(request.META.get("HTTP_AUTHORIZATION", "Basic $")).split("Basic")[1].strip()
    # # # print(f"username: {}; password: {token.split(' ')[1]}")  # admin admin
    # #
    # username = token.split(' ')[0]
    # password = token.split(' ')[1]
    # #
    # user = authenticate(username=username, password=password)
    # print(f"user: {user} | {type(user)}")

    # if (user):
    #     update_last_login(sender=None, user=user)
    #
    #     refresh = RefreshToken.for_user(user=user)
    #     print(f"RefreshToken: {refresh}")
    #
    #     tokens = dict(refresh_token=str(refresh), access_token=str(refresh.access_token))
    # else:
    #     tokens = {}
    # response = {"response": {
    #     "refresh": str(refresh),
    #     "access": str(refresh.access_token),
    #     "token": str(refresh.access_token),
    # }}

    # class TokenNew:
    #     # ...
    #     def __init__(self, user):
    #         token = user
    #
    #     def __str__(self):
    #         return f"{token}"

    return Response(data={"response": "Успешно. get_data", "tokens": tokens}, status=status.HTTP_200_OK)


def send_email_to_new():
    pass


@api_view(http_method_names=["GET", "POST"])
# @permission_classes([AllowAny])  # Все пользователи
@permission_classes([IsAuthenticated])  # Только авторизованные пользователи
def get_public_books(request):
    # print(f"request.user: {request.user}")
    # profile = models.Profile.objects.get(user=request.user)
    # print(f"profile: {profile}")
    #
    # # print(f"profile 1: {request.user.profile}")  # так сделать нельзя
    # print(f"profile 2: {request.user.profile2}")

    page = request.GET.get("page", 1)
    limit = request.GET.get("limit", 5)

    obj_list = models.ModelBook.objects.filter(is_view=True)
    count = len(obj_list)
    paginator_instanse = Paginator(obj_list, limit)
    obj_list = paginator_instanse.get_page(number=page).object_list

    # list1 = []
    # for obj in obj_list:
    #     serialized_obj_list = serializers.BookSerializer(instance=obj, many=False).data
    #     list1.append(serialized_obj_list)
    # return list1

    serialized_obj_list = serializers.BookSerializer(instance=obj_list, many=True).data

    return Response(
        data={"object_list": serialized_obj_list, "count": count},
        status=status.HTTP_200_OK
    )


@api_view(http_method_names=["GET"])
# @permission_classes([AllowAny])  # Все пользователи
@permission_classes([IsAdminUser])  # Только авторизованные пользователи
def get_private_books(request):
    print(f"request.user: {request.user}")

    page = request.GET.get("page", 1)
    limit = request.GET.get("limit", 5)

    obj_list = models.ModelBook.objects.filter(is_view=False)
    count = len(obj_list)
    paginator_instanse = Paginator(obj_list, limit)
    obj_list = paginator_instanse.get_page(number=page).object_list

    serialized_obj_list = serializers.BookSerializer(instance=obj_list, many=True).data

    return Response(
        data={"object_list": serialized_obj_list, "count": count},
        status=status.HTTP_200_OK
    )


@api_view(http_method_names=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"])
# @permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def top(request):
    time.sleep(2)

    if request.method == "GET":  # получение книг

        from django.core.paginator import Paginator
        page = request.GET.get("page", 1)
        limit = request.GET.get("limit", 5)
        search = request.GET.get("search", "")

        # search / filter / order_by
        if search:
            books = models.ModelBook.objects.filter(title__contains=str(search))
        else:
            books = models.ModelBook.objects.all()  # .filter().order_by()  # order_by filter ... # [1, 2, 3, 4, 5 ... 500]

        count = len(books)
        for i in books:
            print(i.return_clear_data())
        paginator_instanse = Paginator(books, limit)  # [1, 2, 3, 4, 5]
        books = paginator_instanse.get_page(number=page).object_list

        serialized_books = serializers.BookSerializer(instance=books, many=True).data
        return Response(data={"object_list": serialized_books, "count": count}, status=status.HTTP_200_OK)
    elif request.method == "POST":  # создание книги

        print(request.POST)
        print(request.FILES)

        # title = request.POST.get("title", "Шаблон заголовка")
        # description = request.POST.get("description", "Шаблон описания")
        # models.ModelBook.objects.create(
        #     title=title,
        #     description=description
        # )

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
