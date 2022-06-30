from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate

from . import models
from . import serializers

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def home(request):
    context = {}
    return render(request, 'build/index.html', context)


def test(request):
    context = {}
    return render(request, 'public/index.html', context)


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
@csrf_exempt
def get_users(request):
    if request.method == "POST":  # create
        pass
    if request.method == "GET":  # read one object / read list of objects
        pass
    if request.method == "PUT":  # update
        pass
    if request.method == "DELETE":  # delete
        pass


    # ingredients = models.ReceiptIngredient.objects.all()
    # serialized_ingredients = serializers.IngredientSerializer(instance=ingredients, many=True)
    # return Response({"ingredients": serialized_ingredients.data})

    # ручная сериализация
    # ingredients = []
    # for i in models.ReceiptIngredient.objects.all():
    #     ingredient = {
    #         "name": i.name,
    #     }
    #     ingredients.append(ingredient)
    # return JsonResponse({"ingredients": ingredients})

    # получаем объекты (строка) с базы
    users_from_db = User.objects.all()
    print(users_from_db)
    print(type(users_from_db))  # QuerySet <class 'django.db.models.query.QuerySet'>

    # сериализуем(превращаем в удобоваримый вариант для JSON) данные
    serialized_users = serializers.UserSerializer(instance=users_from_db, many=True).data  # JSON
    print(serialized_users)
    print(type(serialized_users))  # JSON <class 'rest_framework.utils.serializer_helpers.ReturnList'>

    # возвращаем данные через DRF
    return Response({"ingredients": serialized_users})  # Response(JSON)


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
@csrf_exempt
def get_users_count(request):
    users = User.objects.all().count()
    return JsonResponse({"users": users})


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
@csrf_exempt
def create_user(request):
    # логика создания пользователя

    # print(f"request : {request}")
    # print(f"request.POST : {request.POST}")

    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    print(f"username == {username}")
    print(f"password == {password}")

    User.objects.create(
        username=username,
        password=password,
        email=""
    )

    value = True

    # логика создания пользователя
    return JsonResponse({"result": "Пользователь успешно создан!"})


@api_view(http_method_names=["GET", "POST", "PUT", "DELETE"])
@permission_classes([AllowAny])
@csrf_exempt
def check_user(request):
    if request.method == "GET":
        try:
            username = request.GET.get("username", "")
            User.objects.get(username=username)
            return JsonResponse({"result": "Пользователь успешно проверен!"})
        except Exception as error:
            return JsonResponse({"result": "Пользователя не существует!"})
    else:
        return JsonResponse({"result": "Такой метод не реализован!"})


@api_view(http_method_names=["GET", "POST", "PUT", "DELETE"])
@permission_classes([AllowAny])
@csrf_exempt
def login_user(request):
    if request.method == "POST":
        try:
            username = request.POST.get("username", None)
            print(username)
            password = request.POST.get("password", None)
            print(password)
            apps = request.POST.get("apps", None)
            if apps is not None:
                print('have data')
            print(apps)
            someText = request.POST.get("someText", None)
            print(someText)
            
            user = authenticate(username=username, password=password)
            print(user)
            print(type(user))
            
            if user:
                # сериализуем(превращаем в удобоваримый вариант для JSON) данные
                serialized_user = serializers.UserSerializer(instance=user, many=False).data  # JSON
                print(serialized_user)
                print(type(serialized_user))  # JSON <class 'rest_framework.utils.serializer_helpers.ReturnList'>

                # возвращаем данные через DRF
                return Response({"result": serialized_user})  # Response(JSON)
            else:
                return Response({"result": "Некорректные данные! Проверьте пароль!"})
        except Exception as error:
            return JsonResponse({"result": "Некорректные данные!"})
    else:
        return JsonResponse({"result": "Такой метод не реализован!"})


@api_view(http_method_names=["GET", "POST", "PUT", "DELETE"])
@permission_classes([AllowAny])
@csrf_exempt
def chat_create(request):
    try:
        text = request.POST.get("text", None)
        if text:
            models.TextModel.objects.create(
                text=text
            )
            return JsonResponse({"result": "Сообщение успешно отправлено!"})
        return JsonResponse({"result": "ошибка отправки!"})
    except Exception as error:
        print(f"Error(chat_create): {error}")
        return JsonResponse({"result": "ошибка отправки!"})

@api_view(http_method_names=["GET", "POST", "PUT", "DELETE"])
@permission_classes([AllowAny])
@csrf_exempt
def chat_read(request):
    try:
        texts = models.TextModel.objects.all()
        serialized_texts = serializers.TextModelSerializer(instance=texts, many=True).data
        return JsonResponse({"result": serialized_texts})
    except Exception as error:
        print(f"Error(chat_create): {error}")
        return JsonResponse({"result": []})

@api_view(http_method_names=["GET", "POST", "PUT", "DELETE"])
@permission_classes([AllowAny])
@csrf_exempt
def chat_read_id(request, sms_id):
    
    fake_dict = {f"text {sms_id}": "the some text", "id": sms_id}
    list1 = [{f"text {x}": "the some text", "id": x} for x in range(1, 100)]
    
    # list1 = []
    # for x in range(1, 100):
    #     list1.append({f"text {x}": "the some text", "id": x})
    
    return JsonResponse({"result": {"one": fake_dict, "list": list1}})
