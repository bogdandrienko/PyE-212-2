from operator import concat

from django import template

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
        return str(round(value/60, 2)) + " hours"
    return str(value) + " mins"
