sudo apt-get update -y
sudo apt upgrade -y

 # для входа через ssh 
sudo apt -y install openssh-server
sudo systemctl start ssh
sudo systemctl enable ssh

 # ssh терминал можно скачать на bitvise.com/ssh-client-download 
 # посмотреть ip. где inet 192.168.80.130/   отерываем ssh  в вкладке login -> Host: 192.168.80.130  Port:22  Username: ubuntu или(temir) password: ******
ip a 
sudo adduser temir vboxsf //не импользовал

sudo apt -y install net-tools htop git curl nginx     // установка nginx git. htop - это посмотреть производительность. curl - для запросов 
sudo apt -y install gunicorn python3-pip python3-dev python3-venv build-essential libpq-dev unixodbc-dev postgresql postgresql-contrib


    //не нужно для развертывания
        sudo apt -y install nodejsp
        sudo snap install --classic certbot // сертификат https
        sudo snap install gh // вспомогательный cli для гита
        

# для nginx права пользователя по стандарту www-data  и мы даём нашему пользователю такие же права nginx имел все права
# sudo usermod -aG bogdan www-data

sudo usermod -aG root www-data  
#sudo usermod -aG ubuntu www-data  
# sudo usermod -aG temir www-data  
sudo reboot

ip a

cd ~
mkdir web
cd web
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install wheel
    #Pillow для статики картинок,  django-cors-headers межсайтовые запросы, pyodbc для подключения бд разных, gunicorn распределение нагрузок как балансировщик 
pip install Django gunicorn psycopg2 pyodbc django-cors-headers Pillow
pip install -r requirements.txt
    # django-admin startproject backend_settings .    // это когдв новый, но у нас pip install -r requirements.txt

sudo su - postgres
createuser djangouser
createdb homeworkdb -O djangouser

psql homeworkdb

alter user djangouser with password '12345678Django$';

\q

exit

# после подключения к базе надо сделать миграции
# создание миграций к базе данных
python3 manage.py makemigrations

# применение миграций к бд
python3 manage.py migrate

    # http://0.0.0.0:8000/ в virtual bokse запустить
python3 manage.py createsuperuser




# GUNICORN  настройка  GUNICORN цепляется к Jango, а nginx к  GUNICORN

sudo nano /etc/systemd/system/gunicorn.socket
<file>
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
</file>



sudo nano /etc/systemd/system/gunicorn.service
<file>
[Unit]
Description=Gunicorn for the Django example project
Requires=gunicorn.socket
After=network.target

[Service]
Type=notify


#User=ubuntu
User=root
Group=www-data

RuntimeDirectory=gunicorn
# WorkingDirectory=/home/ubuntu/projects/mytodolist
WorkingDirectory=/root/web
#ExecStart=/home/ubuntu/projects/mytodolist/env/bin/gunicorn --workers 3 --bind unix:/run/gunicorn.sock settings.wsgi:application

ExecStart=/root/web/env/bin/gunicorn --workers 3 --bind unix:/run/gunicorn.sock settings.wsgi:application
#ExecStart=/root/web/env/bin/gunicorn django_settings.wsgi




ExecReload=/bin/kill -s HUP $MAINPID
KillMode=mixed
TimeoutStopSec=5
PrivateTmp=true

[Install]
WantedBy=multi-user.target
</file>

#settings.wsgi:application проверить settings путь правильный

sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable --now gunicorn.service
sudo systemctl daemon-reload
sudo systemctl restart gunicorn

# sudo systemctl status gunicorn.service
# sudo systemctl disable gunicorn
# sudo systemctl stop gunicorn


              #ip77.240.38.106

# sudo nano /etc/nginx/sites-available/192.168.1.83-http.conf 
sudo nano /etc/nginx/sites-available/ilusa.kz
<file>
server {
listen 80;
listen [::]:80;

#server_name localhost 127.0.0.1 192.168.1.83;  
server_name localhost 127.0.0.1 ilusa.kz;  


#root /home/ubuntu/projects/mytodolist;
root /home/ubuntu/web;

# index index.html;

location /.well-known/acme-challenge/ {}

location /favicon.ico {
    #alias /home/ubuntu/projects/mytodolist/static/logo.png;
    alias /home/ubuntu/web/static/logo.png;

    access_log off; log_not_found off;

    expires max;
}

location /robots.txt {
    #alias /home/ubuntu/projects/mytodolist/static/robots.txt;
    alias /home/ubuntu/web/static/robots.txt;

    access_log off; log_not_found off;

    expires max;
}

location /static/ {
    #alias /home/ubuntu/projects/mytodolist/static/;
    alias /home/ubuntu/web/static/;

    expires max;
}

location /media/ {
    #alias /home/ubuntu/projects/mytodolist/static/media/;
    alias /home/ubuntu/web/static/media/;

    expires max;
}

location / {
#    include proxy_params;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header Host $http_host;
    proxy_redirect off;
    proxy_buffering off;
    proxy_pass http://unix:/run/gunicorn.sock;
}
}
</file>

# sudo ln -s /etc/nginx/sites-available/192.168.1.83-http.conf /etc/nginx/sites-enabled/192.168.1.83-http.conf
sudo ln -s /etc/nginx/sites-available/ilusa.kz /etc/nginx/sites-enabled/ilusa.kz
sudo service nginx start
# sudo systemctl status nginx.service
# sudo ufw allow 443
# sudo ufw allow 8000
sudo ufw allow 'Nginx Full'
sudo systemctl reload nginx.service
#последний этап
# sudo nginx -t

sudo reboot

STATIC_URL = '/static/'
STATIC_ROOT = Path(BASE_DIR / 'static')
STATIC_DIR = Path(BASE_DIR / 'static')
STATICFILES_DIRS = [
    Path(BASE_DIR / 'static_external'),
    # Path(BASE_DIR / 'static')
]





python3 manage.py collectstatic

python3 manage.py runserver 0.0.0.0:8000


# разворачиваем на хероку и убунту
# https://www.youtube.com/watch?v=pV1DuzxPJFw&list=PLFH0jFGRecS0btzEqlp6f4Ua8FwJYkH1m&index=33



# https://www.youtube.com/watch?v=iWyblcEi7Bk&list=PLFH0jFGRecS0btzEqlp6f4Ua8FwJYkH1m&index=1
# https://www.youtube.com/watch?v=pV1DuzxPJFw&t=10098s




#сети убунта
#https://www.youtube.com/watch?v=EiB0h0NmFMs&list=PLFH0jFGRecS3toJcJNUPxe8QVO3EeIIDH&index=2&t=3s










# мое решение ошибку даёт

sudo certbot --nginx -d 185.116.193.191 -d www.185.116.193.191




Qwe123

https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04

https://github.com/bogdandrienko/python-jsx-smart-pmp-app/blob/main/web-platform_22_05_dev/scripts/lin_0_create.sh


ювикорн ssl итд