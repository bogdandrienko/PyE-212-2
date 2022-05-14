from django.shortcuts import render
from django.http import HttpResponse
from . import models


# тут только "логика" - функции для обработки и возврат данных

def index(request):
    return render(request, 'app_teacher/pages/index.html')


def home(request):
    return render(request, 'app_teacher/pages/home.html')


def about(request):
    return render(request, 'app_teacher/pages/about.html')


def origin_home(request):
    return render(request, 'app_teacher/pages/origin_home.html')


def todo_detail(request, todo_id):
    obj = models.Task.objects.get(id=todo_id)
    context = {
        "todo": obj
    }
    return render(request, 'app_teacher/pages/DetailTodo.html', context)


def todo_list(request):
    print(request)
    if request.method == "GET":
        print("это GET запрос")
    if request.method == "POST":
        print("это POST запрос")
    if request.method == "PUT":
        print("это PUT запрос")
    if request.method == "DELETE":
        print("это DELETE запрос")

    # print("request.method: ", request.method)
    # print("request.path: ", request.path)
    # print("request.headers: ", request.headers)
    # print("request.META: ", )

    # пробегаемся по ключам словаря
    # for key, value in request.META.keys():

    # пробегаемся по значениям словаря
    # for key, value in request.META.values():

    # пробегаемся по парам: ключ-значение
    # for key, value in request.META.items():
    #     print(f"{key}: {value}")
    # print("request.data: ", request.data)
    # print("request.GET: ", request.GET)

    is_completed = False
    if is_completed:
        pass
    else:
        pass

    list = [1, 2, 3]
    for i in list:
        index = list.index(i)
        # print(i)
        pass

    obj = models.Task.objects.all()

    print(f"obj: {obj}")
    print(f"obj count: {obj.count()}")

    context = {"list": obj}

    return render(request, 'app_teacher/pages/todo_list.html', context)


def todo_create(request):
    print("todo_create")
    if request.method == "POST":
        print("это POST запрос")

        # вызывается Exception (исключение)
        # title = request.POST["title"]
        title1 = request.POST.get("title", "заголовок по умолчанию")
        description1 = request.POST.get("description", "описание по умолчанию")

        obj = models.Task.objects.create(
            title=title1,
            description=description1
        )
        obj.save()


        # приём и обработка данных
    context = {}
    return render(request, 'app_teacher/pages/CreateTodo.html', context)