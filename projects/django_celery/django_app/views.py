from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User, Group

from django.views.decorators.cache import cache_page
from django.core.cache import caches
from django.db import connection, transaction

from django_app import celery as current_celery
from celery.result import AsyncResult
from django_settings.celery import app as celery_app

LocMemCache = caches["default"]
DatabaseCache = caches["special"]


# RedisCache = caches["extra"]


# @transaction.atomic()
@transaction.non_atomic_requests()
def index(request):
    try:
        transaction.savepoint('create user')
        User.objects.create(username="Admin")
        print(1 / 0)  # error
    except Exception as error:
        print(error)
        transaction.savepoint_rollback('create user')
        # transaction.rollback()
    else:
        transaction.savepoint_commit('create user')
        # transaction.commit()
    finally:
        pass

    connection.autocommit = False
    cursor = connection.cursor()

    try:
        connection.autocommit = False
        cursor.execute("insert into zarplata (username, salary) VALUES ('Bogdan5', '666');")
        # cursor.execute("insert into zarplata (username, salary) VALUES ('Bogdan', '666');")

        # print(10 / 0)
        # connection.commit()
    except Exception as error:
        print(f"ERROR: {error}")
        connection.rollback()
    else:
        pass
    finally:
        connection.close()
        cursor.close()

    users_list = [{"username": f"{user.username}", "email": f"{user.email}"} for user in User.objects.all()]
    return JsonResponse(data=users_list, safe=False)


def home(request):

    task_id = current_celery.send_mass_email.apply_async([1, 2, 3], {}, skip_error=True, countdown=20)  #
    old_task_id = "33779111-0f42-4a96-bdec-d5643e57a018"

    result = AsyncResult(old_task_id, app=celery_app)
    # print()

    if result.state != "PENDING":
        result = f"status: {result.state} | result: {result.get()}"
    else:
        result = f"status: {result.state} | result: {None}"
    print(result)

    return JsonResponse(data=f"<h1>task_id: {task_id} | {result}</h1>", safe=False)


# @cache_page(120)
def users(request):
    # old: 60 sec = 1000 users = 1000 BAD REQUEST | timeout=30
    # new: 60 sec = 1000 users = 2 BAD REQUEST | timeout=30

    print("\n\n\n\n\n**********************\n\n\n\n")
    users_list = LocMemCache.get("users")
    if users_list is None:
        # BAD ! COMPUTE request ! BAD
        users_list = [{"username": f"{user.username}", "email": f"{user.email}"} for user in User.objects.all()]
        # BAD ! COMPUTE request ! BAD
        print('BAD ! COMPUTE request ! BAD')
        LocMemCache.set("users", users_list, timeout=30)  # set cache

    print("cache users: ", users_list)
    # print(users_list)

    return JsonResponse(data=users_list, safe=False)
