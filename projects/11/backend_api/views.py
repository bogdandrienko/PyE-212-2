import random
import time
import re

from django.contrib.auth.hashers import make_password
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpRequest
import datetime
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


# Create your views here.

def index(request):
    try:
        return render(request, "index.html", context={})
    except Exception as error:
        if settings.DEBUG:
            print(f"error {error}")
        return render(request, "components/404.html", context={})


@api_view(http_method_names=["GET"])
@permission_classes([AllowAny])  # @permission_classes([IsAuthenticated])
def receipt(request: HttpRequest) -> Response:
    # books = models.ModelBook.objects.all()
    # получить все -- TODO select * from ...

    # books = models.ModelBook.objects.order_by('-update_datetime_field', 'title')
    # сортировка -- TODO ORDER BY update_datetime_field DESC, title ASC

    # books = models.ModelBook.objects.filter(is_view=True)
    # условие -- TODO WHERE is_view = 'True' and BETWEEN 2022-09-27 12:00:00 and 2022-09-29 23:59:59
    # .exclude(name='Eva Smith')
    # .select_related('school')
    # books = models.ModelBook.objects.filter(is_view=True)

    # books = models.ModelBook.objects.all()[:2]
    # ограничение по количеству строк -- TODO SELECT * FROM  (SELECT * as R FROM employees) WHERE R <= 2;

    # TODO models.ModelBook.objects.only("first_name", "last_name")
    # ограничение по включению полей -- TODO SELECT id, title, author, rating FROM Receipt;
    # ВЗЯТЬ ТОЛЬКО ЭТИ ПОЛЯ

    # TODO !!!!!
    # ограничение по исключению полей -- TODO SELECT id, title, author, rating FROM Receipt;
    # ВЗЯТЬ ВСЕ ПОЛЯ, КРОМЕ ЭТИХ

    # b = models.Receipt(title='Beatles Blog', author='Alice').save()
    # ограничение по выборке полей --

    # data = {
    #     "id": 9999,
    #     "is_liked": True,
    #     "rating_value": 4,
    #     "receipt": models.Receipt.objects.get(id=1),
    #     "user": User.objects.get(id=1)
    # }
    # models.ReceiptRating.objects.create(
    #     id=data["id"],
    #     is_liked=data["is_liked"],
    #     rating_value=data["rating_value"],
    #     receipt=data["receipt"],
    #     user=data["user"],
    # )
    # TODO INSERT INTO django_db.backend_api_receiptrating (id, is_liked, rating_value, receipt_id, user_id) VALUE ('4444', '1', '4', '1', '1');
    # вставка строки

    receipts = models.ReceiptRating.objects.filter(id__gte=500)
    for i in receipts:
        receipts.delete()
    # TODO DELETE from django_db.backend_api_receiptrating table1 where table1.id > '500';
    # удаление строки

    # START
    # TRANSACTION;
    #
    # set @ val = '2008';
    #
    # INSERT
    # INTO
    # django_db.backend_api_receiptrating
    # (id, is_liked, rating_value, receipt_id, user_id)
    #
    #
    # VALUE
    # (@ val, '1', '4', '1', '1');
    #
    # select
    # case @ val % 2
    # when
    # 0
    # then
    # ROLLBACK
    # else
    # COMMIT
    # end
    # транзакции

    # datas = [
    #     {
    #         "id": 12222,
    #         "is_liked": True,
    #         "rating_value": 6,
    #         "receipt": models.Receipt.objects.get(id=1),
    #         "user": User.objects.get(id=1)
    #     },
    #     {
    #         "id": 12223,
    #         "is_liked": True,
    #         "rating_value": 5,
    #         "receipt": models.Receipt.objects.get(id=1),
    #         "user": User.objects.get(id=1)
    #     },
    #     {
    #         "id": 12224,
    #         "is_liked": True,
    #         "rating_value": 4,
    #         "receipt": models.Receipt.objects.get(id=1),
    #         "user": User.objects.get(id=1)
    #     },
    # ]
    # for data in datas:
    #     models.ReceiptRating.objects.create(
    #         id=data["id"],
    #         is_liked=data["is_liked"],
    #         rating_value=data["rating_value"],
    #         receipt=data["receipt"],
    #         user=data["user"],
    #     )
    # INSERT
    # INTO
    # django_db.backend_api_receiptrating(id, is_liked, rating_value, receipt_id, user_id)
    # VALUE
    # ('11111', '1', '4', '1', '1'),
    # ('11112', '1', '5', '1', '1'),
    # ('11113', '1', '6', '1', '1');
    # вставка строк

    # receipt_rating = models.ReceiptRating.objects.get(id=500)
    # receipt_rating.rating_value = 10
    # receipt_rating.is_liked = not receipt_rating.is_liked
    # receipt_rating.save()
    # UPDATE
    # django_db.backend_api_receiptrating
    # SET
    # rating_value = '10', is_liked = NOT
    # is_liked - - ABS(is_liked - 1)
    # WHERE
    # id = '500'
    # обновление -- TODO UPDATE;

    # try:
    #     obj = models.ReceiptRating.objects(id=500)
    # except models.ReceiptRating.DoesNotExist:
    #     print('ПРОИЗОШЛА ОШИБКА ИЗ_ЗА ОТСУТСТВИЯ ЗАПИСИ')
    #     obj = models.ReceiptRating(id=500, rating_value=10)
    #     obj.save()
    # except Exception as error:
    #     print('ПРОИЗОШЛА ОШИБКА, НО НЕ ИЗ_ЗА ОТСУТСТВИЯ ЗАПИСИ')

    # receipt_, _ = models.ReceiptRating.objects.get_or_create(id=20001)
    # # receipt_rating = receipt_[0]
    # # ok = receipt_[1]
    # # a, b = (10, None)
    # # a, b = (models.ReceiptRating.objects.get(id=500), True)
    #
    # receipt_.rating_value = 5
    # receipt_.is_liked = not receipt_.is_liked
    # receipt_.receipt = models.Receipt.objects.get(id=1)
    # receipt_.user = User.objects.get(id=1)
    # receipt_.save()
    #
    # INSERT
    # INTO
    # django_db.backend_api_receiptrating
    # (id, is_liked, rating_value, receipt_id, user_id)
    # VALUES
    # (66667, '1', '8', '1', '1')
    # ON
    # DUPLICATE
    # KEY
    # UPDATE
    # is_liked = '1',
    # rating_value = '4',
    # receipt_id = '1',
    # user_id = '1';
    # обновление или вставка -- TODO UPSERT;

    # Student.objects.count() 4
    # количество возвращаемых записей -- TODO SELECT COUNT(*) FROM employee;

    # .all()
    # .first()
    # количество возвращаемых записей -- TODO SELECT TOP 1 * FROM table_Name ORDER BY unique_column DESC; MSSQL

    #  TODO SELECT SUM(price) FROM magazine group by id;

    #  TODO SELECT * FROM table_Name ORDER BY unique_column DESC LIMIT 1;    POSTGRESQL

    #  TODO SELECT * FROM Receipt where time = ( SELECT MAX(time) FROM Receipt )
    #  TODO SELECT * FROM Receipt where id = ( SELECT MAX(id) FROM Receipt )

    #  TODO SELECT LAST_VALUE(id) FROM Receipt

    #  TODO SELECT * FROM Receipt where time = ( SELECT MIN(time) FROM Receipt )
    #  TODO SELECT * FROM Receipt where id = ( SELECT MIN(id) FROM Receipt )

    # / *SELECT * FROM
    # django_db.backend_api_receiptrating; * /
    # / *Receipt.objects.all() * /
    # / *Получить
    # записи * /
    #
    # / *SELECT * FROM
    # django_db.backend_api_receiptrating
    # ORDER
    # BY
    # rating_value
    # ASC, is_liked
    # DESC, receipt_id
    # ASC * /
    # / *Receipt.objects.order_by('-rating_value', '-is_liked', 'receipt') * /
    # / *Сортируем
    # записи * /
    #
    # / *ReceiptRating.objects.filter(rating_value=6) * /
    # / *SELECT * FROM
    # django_db.backend_api_receiptrating
    # WHERE
    # is_liked = '0' and rating_value
    # BETWEEN
    # 0 and 3; * /
    # / *SELECT * FROM
    # django_db.backend_api_receiptrating
    # WHERE
    # rating_value = 1 or rating_value = 2; * / / *1, 5, 7 * /
    # / *Фильтруем
    # записи * /
    #
    # / *SELECT * FROM
    # django_db.backend_api_receiptrating
    # WHERE
    # rating_value in (1, 5, 7); * /
    # / *ReceiptRating.objects.filter(rating_value__in=[1, 5, 7]) * /
    # / *Фильтруем
    # записи * /
    #
    # / *SELECT
    # Count(*)
    # FROM
    # django_db.backend_api_receiptrating
    # WHERE
    # rating_value = 6; * /
    # / *ReceiptRating.objects.filter(rating_value=6).count() * /
    # / *Фильтруем
    # записи * /
    #
    # / *SELECT
    # SUM(rating_value)
    # FROM
    # django_db.backend_api_receiptrating; * /
    # / *SELECT
    # AVG(rating_value)
    # FROM
    # django_db.backend_api_receiptrating; * /
    # SELECT
    # SUM(rating_value * is_liked) / SUM(is_liked)
    # FROM
    # django_db.backend_api_receiptrating;

    #  TODO SELECT SUM(salary * count_people)/SUM(count_people) FROM magazine group by id;

    # receipts = models.Receipt.objects.values_list('id', 'title', 'author') -> *args (1, "Заголовок", "Alice")
    # receipts = models.Receipt.objects.values('id', 'title', 'author') # -> **kwargs {"id": 1, "title": "Заголовок", "author": "Alice"}

    # receipts = models.ReceiptRating.objects.filter(rating_value__in=[1, 5, 7])
    # receipts = models.ReceiptRating.objects.raw('SELECT * FROM django_db.backend_api_receiptrating')
    # for i in receipts:
    #     print(i.rating_value)

    user = 'root'

    # TODO ###############################################################################################
    # TODO pyodbc
    # import pyodbc
    # connection_string = 'DRIVER={Devart ODBC Driver for MySQL};' \
    #                     f'UserID={user};' \
    #                     'Password=mypassword;' \
    #                     'Server=myserver;' \
    #                     'Database=mydatabase;' \
    #                     'Port=myport;' \
    #                     'String Types=Unicode'
    # connection = pyodbc.connect(connection_string)
    # cursor = connection.cursor()

    # connection.autocommit = True # !!!!!! автосохранение изменений и транзакций
    # cursor.execute("INSERT INTO EMP (EMPNO, ENAME, JOB, MGR) VALUES (535, 'Scott', 'Manager', 545)")
    # connection.commit() # сохранить изменения
    # connection.rollback() # откатить изменения

    # cursor.execute("select * from ")
    # rows = cursor.fetchall()
    # print(rows)
    # cursor.close()
    # connection.close()
    # TODO pyodbc
    # TODO ###############################################################################################

    # TODO ###############################################################################################
    # TODO psycopg2
    # import psycopg2
    # connection_string = 'DRIVER={Devart ODBC Driver for MySQL};' \
    #                     f'UserID={user};' \
    #                     'Password=mypassword;' \
    #                     'Server=myserver;' \
    #                     'Database=mydatabase;' \
    #                     'Port=myport;' \
    #                     'String Types=Unicode'
    # connection = psycopg2.connect(connection_string)
    # cursor = connection.cursor()

    # connection.autocommit = True !!!!!! автосохранение изменений и транзакций
    # cursor.execute("INSERT INTO EMP (EMPNO, ENAME, JOB, MGR) VALUES (535, 'Scott', 'Manager', 545)")
    # connection.commit() # сохранить изменения
    # connection.rollback() # откатить изменения

    # cursor.execute("select * from ")
    # rows = cursor.fetchall()
    # print(rows)
    # cursor.close()
    # connection.close()
    # TODO psycopg2
    # TODO ###############################################################################################

    # TODO ###############################################################################################
    # TODO django.db.connection
    # from django.db import connection
    # cursor = connection.cursor()

    # connection.autocommit = True  # !!!!!! автосохранение изменений и транзакций
    # cursor.execute("INSERT INTO EMP (EMPNO, ENAME, JOB, MGR) VALUES (535, 'Scott', 'Manager', 545)")
    # connection.commit()  # сохранить изменения
    # connection.rollback()  # откатить изменения

    # cursor.execute("select * from ")
    # rows = cursor.fetchall()
    # print(rows)
    # cursor.close()
    # connection.close()
    # TODO django.db.connection
    # TODO ###############################################################################################

    # for i in receipts:
    #     print(i)

    # for x in range(1, 1000):
    #
    #     random_user = User.objects.get(id=random.randint(1, 2))  # Admin | Bogdan
    #     random_bool = random.randint(0, 1) % 2 == 0  # True | False
    #     random_int = random.randint(1, 10)  # 1 .... 10
    #     random_receipt = models.Receipt.objects.get(id=random.randint(1, 2))  # 1 | 2
    #
    #     models.ReceiptRating.objects.create(
    #         is_liked=random_bool,
    #         rating_value=random_int,
    #         user=random_user,
    #         receipt=random_receipt,
    #     )

    # print("\n\n\n!!!\n")
    # print(f"receipts: {receipts}")
    # print("\n\n\n!!!\n")

    # receipts = models.Receipt.objects.all()
    # receipts_serialized = serializers.ReceiptSerializer(instance=receipts, many=True).data

    # print(receipts_serialized)

    # return Response(data={"ответ:": receipts_serialized}, status=status.HTTP_200_OK)

    return Response(data={"ответ:": ""}, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET", "POST", "PUT"])
@permission_classes([AllowAny])
def registration(request):
    if request.method == "GET":
        return Response(data={"ответ:": r'(POST){"email": "admin@gmail.com", "password": "12345qwe!Brty"} '
                                        '=> <Response 201>'},
                        status=status.HTTP_200_OK)
    elif request.method == "POST":
        try:
            email = request.data.get("email", None)
            password = request.data.get("password", None)
            if email and password:
                if re.match(r"^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", password) and \
                        re.match(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", email):
                    User.objects.create(
                        username=email,
                        email=email,
                        password=make_password(password)  # для create НУЖНО шифровать пароль, для create_user НЕТ!
                    )
                    return Response(status=status.HTTP_201_CREATED)
                else:
                    return Response(data={"ответ:": "Вы не прошли проверку регулярного выражения"},
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response(data=str(error), status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(
            data={"response": "метод не реализован"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )
