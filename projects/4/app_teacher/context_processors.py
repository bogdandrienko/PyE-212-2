from . import models


def receipt_count(request):
    return dict(receipt_count=models.Receipt.objects.all().count)
