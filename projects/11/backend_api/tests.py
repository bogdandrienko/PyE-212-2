from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from backend_api import models, serializers


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
    def setUp(self):  # настройки перед тестированием
        print('Преднастройка для test_model_create')
        # CustomTest.run_test()  # наш собственный класс для тестов

        models.ReceiptCategory.objects.create(title="title 1")
        models.ReceiptCategory.objects.create(title="title 2")

    def test_model_create(self):
        """Тестируем модель на корректное создание"""
        print('test_model_create')
        title_1 = models.ReceiptCategory.objects.get(title="title 1")
        title_2 = models.ReceiptCategory.objects.get(title="title 2")

        self.assertEqual(title_1.test_get_title(), f'title 1')
        # self.assertEqual(title_2.test_get_title(), f'1 title 2')


class GetActiveUserListViewTestCase(TestCase):
    def setUp(self):
        print('Преднастройка для GetActiveUserListViewTestCase')

        User.objects.create(
            username="admin@admin.ru",
            email="admin@admin.ru",
            password=make_password("12345qwerty!#@")
        )

    def test_api_registration_get(self):
        """Тестируем класс на корректный возврат значений"""

        print('test_api_registration_get')

        client = Client()
        response = client.get(reverse('registration'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_check_users(self):
        """Тестируем класс на корректный возврат значений"""

        print('test_check_users')

        # обращаемся к  маршруту и контроллеру
        client = Client()
        response = client.get(reverse('get_active_user_list'))

        # обращаемся к базе за данными для сравнения
        users = User.objects.filter(is_active=True)
        ser_users = serializers.UserSerializer(instance=users, many=True).data
        obj = {"user_list": ser_users}

        # сравнение данных
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, obj)

    def test_api_registration_post(self):
        """Тестируем класс на корректный возврат значений"""

        print('test_api_registration_post')

        # обращаемся к  маршруту и контроллеру
        client = Client()
        response1 = client.post(
            reverse('registration'),
            data={
                "email": "admin1@gmail.com",
                "password": "qwe!Brty"
            }
        )

        # сравнение данных
        response2 = client.post(
            reverse('registration'),
            data={
                "email": "admin1@gmail.com",
                "password": "1214124123qwe!Brty"
            }
        )
        print(response2.data)

        response3 = client.put(
            reverse('registration'),
            data={
                "email": "admin1@gmail.com",
                "password": "12424qwe!Brty"
            }
        )
        print(response3.data)
        print(response3.status_code)

        # сравнение данных
        self.assertEqual(response1.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response3.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


if __name__ == "__main__":
    CustomTest.run_test()
