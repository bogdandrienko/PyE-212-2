from . import models


def todo_count(request):
    dict1 = dict(todo_count=0)

    dict2 = {}
    dict2["todo_count"] = models.Task.objects.all().count
    return dict2
