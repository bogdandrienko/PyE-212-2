from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.utils import timezone

from . import models
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.urls import reverse


def home(request, filter_category=""):
    if request.user.is_authenticated is False:
        return redirect(reverse('login', args=()))
    # return HttpResponse("<h1>HOME PAGE</h1>")

    categories = models.ReceiptCategory.objects.all()

    # receipts = models.Receipt.objects.all().filter(category=models.ReceiptCategory.objects.get(title="Борщ"))
    receipts = models.Receipt.objects.all()
    print(receipts)
    print(type(receipts))
    print(receipts[0].description)
    print(type(receipts[0].description))
    print("\n\n**********\n\n")

    if filter_category:
        receipts1 = []
        for receipt in receipts:
            print(receipt.category.all())
            print(type(receipt.category.all()))
            all_receipts = receipt.category.all()

            # all1 = []
            # for x in all_receipts:
            #     all1.append(x.title)
            all = [x.title for x in all_receipts]  # затолкали в новый массив все заголовки категорий

            if filter_category in all:  # если в массиве есть такая "строка"
                receipts1.append(receipt)
        receipts = receipts1

    context = {"receipts": receipts, "categories": categories}
    return render(request, 'app_teacher/pages/home.html', context)


def receipt(request, receipt_id):
    if request.user.is_authenticated is False:
        return redirect(reverse('login', args=()))
    # return HttpResponse("<h1>HOME PAGE</h1>")

    # receipts = models.Receipt.objects.all().filter(title)

    # receipt = get_object_or_404(models.Receipt, pk=receipt_id)
    receipt = models.Receipt.objects.get(id=receipt_id)
    # print(receipt)
    # print(type(receipt))

    comments = models.ReceiptComment.objects.all().filter(receipt=receipt).order_by('-time', '-comment_text')
    # print(comments)
    # print(type(comments))

    # comments[0].time = timezone.now()
    # comments[0].time.save()

    likes = models.ReceiptRating.objects.all().filter(receipt=receipt)
    # print(likes)
    # print(type(likes))

    obj1 = models.ReceiptRating.objects.filter(
        user=request.user,
        receipt=models.Receipt.objects.get(id=receipt_id),
    )[0]
    print(obj1)
    print(obj1.is_liked)
    if obj1.is_liked is True:
        is_my_like = True
    else:
        is_my_like = False

    context = {"receipt": receipt, "comments": comments, "likes": likes, "is_my_like": is_my_like}
    return render(request, 'app_teacher/pages/receipt.html', context)


def receipt_comment_create(request, receipt_id: int):
    if request.method == "POST":
        comment_text = request.POST.get("comment_text", "")
        if comment_text:
            models.ReceiptComment.objects.create(
                comment_text=comment_text,
                user=request.user,
                receipt=models.Receipt.objects.get(id=receipt_id),
            )

    return redirect(reverse('receipt', args=(receipt_id,)))


def receipt_like_create(request, receipt_id: int):
    # if request.method == "POST":
    #     comment_text = request.POST.get("comment_text", "")
    #     if comment_text:
    #         models.ReceiptComment.objects.create(
    #             comment_text=comment_text,
    #             user=request.user,
    #             receipt=models.Receipt.objects.get(id=receipt_id),
    #         )

    try:
        obj = models.ReceiptRating.objects.filter(
            user=request.user,
            receipt=models.Receipt.objects.get(id=receipt_id),
        )[0]
        print(obj)
        obj.is_liked = not obj.is_liked
        obj.rating_value = 0
        obj.save()
    except Exception as error:
        models.ReceiptRating.objects.create(
            is_liked=True,
            rating_value=0,
            user=request.user,
            receipt=models.Receipt.objects.get(id=receipt_id),
        )

    return redirect(reverse('receipt', args=(receipt_id,)))


def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('home', args=()))
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        print(f'username: {username}')
        print(f'password: {password}')

        user = authenticate(username=username, password=password)
        if user:
            django_login(request, user)
            print("success")
        else:
            print("fail")
    context = {}
    return render(request, 'app_teacher/pages/login.html', context)


def register(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        password2 = request.POST.get("password2", "")
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")
        email = request.POST.get("email", "")

        success = True
        # if not username or not password:
        if username == "" or password == "":
            print("имя пользователя или пароль пустые!")
            success = False

        if password != password2:
            print("пароли не совпадают!")
            success = False

        user = User.objects.get(username=username)
        if user:
            print("пользователь уже существует!")
            success = False

        if success:
            # 1 способ
            obj = User.objects.create(
                username=username,
                password=make_password(password),
                first_name=first_name,
                last_name=last_name,
                email=email,

            )
            obj.save()

            # 2 способ
            # obj = User.objects.create(
            #     username=username,
            #     first_name=username,
            #     last_name=username,
            #     email=username,
            # )
            # obj.set_password(password)
            # obj.save()
    context = {}
    return render(request, 'app_teacher/pages/register.html', context)


@csrf_exempt
def api_result(request):
    if request.method == "POST":
        data = request.POST.get("value", "данные не пришли!")
        print(data)
        return HttpResponse(data)
    # return HttpResponse("Hello world1111111111111111111111!")
    recept_queryset = models.Receipt.objects.all()
    recept_list = []
    for i in recept_queryset:
        recept_list.append(i.title)
    return JsonResponse({"recepts": recept_list})


def api_result_id(request, recept_id):
    try:
        recept_queryset = models.Receipt.objects.get(id=recept_id)
        return JsonResponse({"recepts": recept_queryset.title})
    except Exception as error:
        return JsonResponse({"recepts": "Recept not have!"})
