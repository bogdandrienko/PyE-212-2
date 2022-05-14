# меняет "директорию" на предыдущую, т.к. мы находимся в папке "scripts"

cd ..\

# обновляет "глобально" версию пакетов pip
python.exe -m pip install --upgrade pip

# устанавливает "глобально" библиотеку для создания виртуальных окружений
pip install env

# создаёт виртуальное окружение
python -m venv env

# активация виртуального окружения
call .\env\Scripts\activate.bat

# обновляет "локально" версию пакетов pip
pip install --upgrade pip



# "построчно" читает данные с файла и устанавливает эти библиотеки в активированное виртуальное окружение
pip install -r requirements.txt

# "замораживает" установленные библиотеки из виртуального окружения
pip freeze > requirements.txt



# устанавливает в виртуальное окружение библиотеки "Django" и pillow(для работы с изображениями) установленные библиотеки из виртуального окружения
pip install django
pip install pillow

# создание Django-проекта с именем "settings" в этой же директории
django-admin startproject settings .

# создание Django-приложение с именем "app_second" в этой же директории
django-admin startapp app_second

# Создание суперпользователя
# python manage.py createsuperuser
python manage.py createsuperuser --username Bogdan --email bogdandrienko@gmail.com


# создание миграций к базе данных
python manage.py makemigrations

# применение миграций к бд
python manage.py migrate



# запускает "development"(сервер для разработки) 0.0.0.0:88
python manage.py runserver 127.0.0.1:8000
