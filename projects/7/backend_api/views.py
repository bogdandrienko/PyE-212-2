import random
import time

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
import datetime
import requests
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
from backend_api import serializers
from backend_api import utils


def index(request):
    try:
        return render(request, "build/index.html", context={})
    except Exception as error:
        if settings.DEBUG:
            print(f"error {error}")
        return render(request, "components/404.html", context={})


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def login(request):
    utils.print_data_from_frontend(request=request)

    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        if username and password:
            user = User.objects.get(username=username)
            if user.is_active:
                update_last_login(sender=None, user=user)
                refresh = RefreshToken.for_user(user=user)
                response = {"response": {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token)
                }}
                return Response(response)
            else:
                return HttpResponse(status=status.HTTP_404_NOT_FOUND)
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
@permission_classes([IsAuthenticated])
def categories(request, category_id=0):
    time.sleep(2)

    if int(category_id) >= 1:
        if request.method == "GET":  # получение книги
            book = get_object_or_404(models.ModelBook, id=category_id)
            serialized_book = serializers.BookSerializer(instance=book, many=False).data
            return Response(data=serialized_book, status=status.HTTP_200_OK)
        elif request.method == "DELETE":
            book = models.ModelBook.objects.get(id=category_id).delete()
            book.delete()
            return Response(data={"response": "Успешно удалено."}, status=status.HTTP_200_OK)
        elif request.method == "PUT" or request.method == "PATCH":
            book = models.ModelBook.objects.get(id=category_id)

            title = request.POST.get("title", "Шаблон заголовка")
            description = request.POST.get("description", "Шаблон описания")
            if book.title != title:
                book.title = title
            if book.description != description:
                book.description = description
            book.save()

            book = models.ModelBook.objects.get(id=category_id)
            serialized_book = serializers.BookSerializer(instance=book, many=False).data
            return Response(data=serialized_book, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    else:
        if request.method == "GET":
            categories_list = models.ModelBookCategory.objects.all()
            serialized_categories = serializers.BookCategorySerializer(instance=categories_list, many=True).data
            return Response(data={"object_list": serialized_categories}, status=status.HTTP_200_OK)
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
@permission_classes([IsAuthenticated])
def top(request):
    time.sleep(2)

    if request.method == "GET":  # получение книг

        page = request.GET.get("page", 1)
        limit = request.GET.get("limit", 5)

        books = models.ModelBook.objects.filter(is_view=True).order_by('-update_datetime_field', 'title')

        search = request.GET.get("search", "")
        if search:
            books = books.filter(title__contains=str(search))

        filter = request.GET.get("filter", "")
        if filter:

            def get_fresh(is_new: bool, books_arg):
                new_books = []
                target_time = datetime.datetime.now() + datetime.timedelta(hours=-6, minutes=-1)
                for book in books_arg:
                    # print(f"""{i.update_datetime_field.strftime("%m/%d/%Y, %H:%M:%S")}  {target_time.strftime("%m/%d/%Y, %H:%M:%S")} {i.update_datetime_field.strftime("%m/%d/%Y, %H:%M:%S") > target_time.strftime("%m/%d/%Y, %H:%M:%S")}""")
                    if is_new:
                        if book.update_datetime_field.strftime("%m/%d/%Y, %H:%M:%S") > \
                                target_time.strftime("%m/%d/%Y, %H:%M:%S"):
                            new_books.append(book)
                    else:
                        if book.update_datetime_field.strftime("%m/%d/%Y, %H:%M:%S") < \
                                target_time.strftime("%m/%d/%Y, %H:%M:%S"):
                            new_books.append(book)
                return new_books

            if filter == "меньше минуты назад":
                books = get_fresh(True, books)
            elif filter == "больше минуты назад":
                books = get_fresh(False, books)
            else:
                pass

        category = request.GET.get("category", "")
        if category:
            try:
                category_obj = models.ModelBookCategory.objects.get(title=category)
                books = [book for book in books if category_obj in book.category.all()]
            except Exception as error:
                pass

        utils.print_data_from_frontend(request=request)

        # return Response(status=status.HTTP_404_NOT_FOUND)
        # return Response(status=status.HTTP_401_UNAUTHORIZED)

        # books = models.ModelBook.objects.all()
        # получить все -- TODO select * from ...

        # books = models.ModelBook.objects.order_by('-update_datetime_field', 'title')
        # сортировка -- TODO ORDER BY update_datetime_field DESC, title ASC

        # books = models.ModelBook.objects.filter(is_view=True)
        # условие -- TODO WHERE is_view = 'True'

        # books = models.ModelBook.objects.all()[:2]
        # ограничение по количеству строк -- TODO SELECT * FROM  (SELECT * as R FROM employees) WHERE R <= 2;
        # TODO SELECT * FROM Universities LIMIT 2

        # response = requests.get("https://jsonplaceholder.typicode.com/todos/")
        # books = response.json()

        count = len(books)
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


#################################################################################

@api_view(http_method_names=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"])
@permission_classes([IsAuthenticated])
def books(request, book_id=0):
    time.sleep(1)

    try:
        if int(book_id) > 0:
            if request.method == "GET":
                book = get_object_or_404(models.ModelBook, id=book_id)
                serialized_book = serializers.BookSerializer(instance=book, many=False).data
                return Response(data={"object": serialized_book}, status=status.HTTP_200_OK)
            elif request.method == "DELETE":

                book = models.ModelBook.objects.get(id=book_id)

                print(f"УДАЛЕНИЕ КНИГИ С ЗАГОЛОВКОМ: {book.title}")
                # book.delete()
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
            if request.method == "GET":
                page = request.GET.get("page", 1)
                limit = request.GET.get("limit", 5)
                books_queryset = models.ModelBook.objects.all()
                count = len(books_queryset)
                paginator_instanse = Paginator(books_queryset, limit)
                books_queryset = paginator_instanse.get_page(number=page).object_list
                serialized_books = serializers.BookSerializer(instance=books_queryset, many=True).data
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
    except Exception as error:
        if settings.DEBUG:
            print(f"error {error}")
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(http_method_names=["GET"])
# @permission_classes([IsAuthenticated])
@permission_classes([AllowAny])
def test(request, test_id=0):
    time.sleep(random.randint(1, 4))

    try:
        if int(test_id) > 0:
            if request.method == "GET":
                response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{test_id}')
                return Response(data={"object": response.json()}, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            if request.method == "GET":
                page = request.GET.get("page", 1)
                limit = request.GET.get("limit", 5)
                books_queryset = requests.get('https://jsonplaceholder.typicode.com/posts').json()
                count = len(books_queryset)
                paginator_instanse = Paginator(books_queryset, limit)
                books_queryset = paginator_instanse.get_page(number=page).object_list
                return Response(data={"object_list": books_queryset, "count": count}, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except Exception as error:
        if settings.DEBUG:
            print(f"error {error}")
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
