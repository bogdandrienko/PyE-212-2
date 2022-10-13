from django.contrib.auth.models import User


def get_users_count(request):
    return {"user_count": User.objects.all().count()}
