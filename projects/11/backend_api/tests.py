from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.test import TestCase
from backend_api import models


# class ReceiptCategory(models.Model):
#     title = models.CharField(
#         primary_key=False,
#         unique=False,
#         editable=True,
#         blank=True,
#         null=True,
#         default="Заголовок",
#         verbose_name="Заголовок:",
#         help_text='<small class="text-muted">это наш заголовок</small><hr><br>',
#
#         max_length=250,
#     )
#
#     class Meta:
#         app_label = 'backend_api'
#         ordering = ('title',)
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории рецептов'
#
#     def __str__(self):  # возвращает строкове представление объекта
#         return f'{self.title}'

class MyTestException(Exception):
    def __init__(self, error_message: str):
        self.error_message = error_message

    def error(self):
        return f"| {self.error_message} |"

class CustomTest:
    @staticmethod
    def run_test():
        try:
            print('test BEGIN')

            # pre
            models.ReceiptCategory.objects.create(title="title 1")
            models.ReceiptCategory.objects.create(title="title 2")

            # equal
            title_1 = models.ReceiptCategory.objects.get(title="title 1")
            title_2 = models.ReceiptCategory.objects.get(title="title 2")

            if title_1.test_get_title() != f'title 1':
                raise MyTestException('проверка 1 не пройдена!')
            if title_2.test_get_title() != f'2 title 2':
                raise MyTestException('проверка 2 не пройдена!')
        except MyTestException as error:
            print(f'run_test MyTestException FAIL : {error}')
        except Exception as error:
            print(f'run_test Exception FAIL : {error}')
        else:
            print('run_test OK')
        finally:
            print('test END')


class ReceiptCategoryModelTestCase(TestCase):
    def setUp(self):
        # models.ReceiptCategory.objects.create(title="title 1")
        # models.ReceiptCategory.objects.create(title="title 2")
        CustomTest.run_test()

    def test_animals_can_speak(self):
        """Тестируем модель на корректное создание"""
        # title_1 = models.ReceiptCategory.objects.get(title="title 1")
        # title_2 = models.ReceiptCategory.objects.get(title="title 2")
        # self.assertEqual(title_1.test_get_title(), f'title 1')
        # self.assertEqual(title_2.test_get_title(), f'1 title 2')

# @api_view(http_method_names=["GET", "POST"])
# @permission_classes([AllowAny])
# def registration(request):
#     if request.method == "GET":
#         return Response(data={"ответ:": r'(POST){"email": "admin@gmail.com", "password": "12345qwe!Brty"} '
#                                         '=> <Response 201>'},
#                         status=status.HTTP_200_OK)
#     elif request.method == "POST":
#         try:
#             email = request.data.get("email", None)
#             password = request.data.get("password", None)
#             if email and password:
#                 if re.match(r"^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", password) and \
#                         re.match(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", email):
#                     User.objects.create(
#                         username=email,
#                         email=email,
#                         password=make_password(password)  # для create НУЖНО шифровать пароль, для create_user НЕТ!
#                     )
#                     return Response(status=status.HTTP_201_CREATED)
#                 else:
#                     return Response(data={"ответ:": "Вы не прошли проверку регулярного выражения"},
#                                     status=status.HTTP_201_CREATED)
#             else:
#                 return Response(status=status.HTTP_400_BAD_REQUEST)
#         except Exception as error:
#             return Response(data=str(error), status=status.HTTP_400_BAD_REQUEST)
#     else:
#         return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class GetActiveUserListViewTestCase(TestCase):
    def setUp(self):
        User.objects.create(
                username="admin@admin.ru",
                email="admin@admin.ru",
                password=make_password("12345qwerty!@")
            )

    def test_animals_can_speak(self):
        """Тестируем класс на корректный возврат значений"""

        import requests

        headers = {"user-agent": "user"}
        response = requests.post(
            url="http://127.0.0.1:8000/api/registration/",
            headers=headers,
            data={
                "email": "admin@admin.ru",
                "password": "12345qwerty!@",
            }
        )

        print(response)
        print(response.status_code)
        print(response.content)
        self.assertEqual(response.status_code, 201)


        # title_1 = models.ReceiptCategory.objects.get(title="title 1")
        # title_2 = models.ReceiptCategory.objects.get(title="title 2")
        # self.assertEqual(title_1.test_get_title(), f'title 1')
        # self.assertEqual(title_2.test_get_title(), f'1 title 2')


if __name__ == "__main__":
    CustomTest.run_test()
