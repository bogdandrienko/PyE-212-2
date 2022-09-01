from django import template

register = template.Library()


@register.filter(is_safe=True)
def safe_password(password: str) -> str:
    """
    Этот фильтр прячет случайно раскрытые пароли!
    """
    if len(password.split(sep='pbkdf2')) > 1:
        result = password
    else:
        result = "Опасность"

    return result


@register.simple_tag(takes_context=True)
def cut_string(context, target_string: str, length=15):
    request = context['request']  # Пользователь, данные, группы, доступы и прочее
    if len(target_string) > length:
        result = target_string[0:length] + '...'
    else:
        result = target_string
    return result
