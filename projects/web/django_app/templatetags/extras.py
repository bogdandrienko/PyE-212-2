from django import template

register = template.Library()


@register.filter(is_safe=True)
def lower_text(target: str) -> str:
    # anything
    return target.lower() + " bananas"


@register.simple_tag(takes_context=True)
def truncate_float(context: any, target: any, count: int) -> str:
    # anything
    request = context["request"]
    try:
        sides = str(target).split('.')
        left = sides[0]
        right = str(sides[1])[0:count:1]

        print(f"{left}.{right}")

        return f"{left}.{right}"
    except Exception as error:
        print(error)
        return target
