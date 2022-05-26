from django import template

register = template.Library()


@register.filter(is_safe=True)
def my_filter(value):
    return str(value).strip()[:-2] + "new new"


@register.simple_tag
def upper_case(value):
    return str(value).upper()


@register.simple_tag
def beautiful_number(value):
    str1 = str(value)

    if len(str1) > 3:
        return str(value)[0:-5:1] + " " + str(value)[-5::1]

    if len(str1) > 6:
        return str(value)[0:-5:1] + " " + str(value)[-5::1] + " " + str(value)[-8::1]


@register.simple_tag
def custom_ceil(number, ndigits):
    return round(number=number, ndigits=ndigits)


@register.simple_tag
def split_string_to_list(string: str, separator: str):
    return str(string).split(separator)
