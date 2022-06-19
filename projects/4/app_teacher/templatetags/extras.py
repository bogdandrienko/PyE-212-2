from operator import concat

from django import template
from django.contrib.auth.models import Group, User

from app_teacher import models

register = template.Library()


@register.filter(is_safe=True)
def substr(desc: str):
    if len(desc) >= 50:
        value = desc[:50:1]
        add = "..."
        # return "%s%s" % (value, add)
        # return f"{}{}".format(value, add)
        # return "{0}{1}".format(value, add)
        # return concat(value, add)
        # return value + add
        return f'{value}{add}'
    else:
        return desc


@register.simple_tag
def time_convert(value, converter):
    if int(value) > int(converter):
        if value % 60 == 0:
            return str(int(value / 60)) + " hours"
        return str(round(value / 60, 2)) + " hours"
    return str(value) + " mins"


@register.simple_tag(takes_context=True)
def check_like(context, receipt_id):
    request = context['request']
    try:
        receipt = models.ReceiptRating.objects.filter(
            user=request.user,
            receipt=models.Receipt.objects.get(id=receipt_id),
        )[0]
        print(receipt)
        print(receipt.is_liked)
        if receipt.is_liked is True:
            return True
        else:
            return False
    except Exception as error:
        return False


@register.simple_tag(takes_context=True)
def check_is_have_group(context, group_name=""):
    request = context['request']
    try:
        # return request.user.groups.filter(name=group_name).exists()  # проверка, что такая группа у пользователя есть
        # return len(request.user.groups.filter(name=group_name)) > 0  # проверка, что групп у этого пользователя с таким именем больше нуля

        user = request.user
        groups = user.groups
        # print(groups)
        # print(type(groups))
        # print(groups.all())
        # print(type(groups.all()))
        # print(User.objects.all())
        # print(type(User.objects.all()))
        for group in groups.all():
            if str(group.name).lower() == str(group_name).lower():
                return True
        return False
    except Exception as error:
        return False

# @register.simple_tag(takes_context=True)
# def current_time(context, format_string):
#     timezone = context['timezone']
#     return your_get_current_time_method(timezone, format_string)
