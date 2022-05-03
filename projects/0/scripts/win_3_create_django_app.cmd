@echo OFF

cd ..\

call .\env\Scripts\activate.bat



django-admin startapp app

python manage.py makemigrations

python manage.py migrate



call cmd