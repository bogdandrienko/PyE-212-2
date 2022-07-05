sudo apt-get update -y
sudo apt upgrade -y

sudo apt -y install openssh-server & systemctl start ssh & systemctl enable ssh

sudo apt -y install htop git curl nginx
sudo apt -y install gunicorn python3-pip python3-dev python3-venv build-essential libpq-dev unixodbc-dev postgresql postgresql-contrib

sudo usermod -aG bogdan www-data

ip a

cd ~
mkdir web
cd web
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install wheel
pip install Django gunicorn psycopg2 pyodbc django-cors-headers Pillow
pip install -r requirements.txt

sudo su - postgres
createuser dbdjango
createdb djangodb -O dbdjango

psql djangodb

alter user dbdjango with password '12345678Django$';

\q

exit



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

User=bogdan
Group=www-data

RuntimeDirectory=gunicorn
WorkingDirectory=/home/bogdan/projects/4
ExecStart=/home/bogdan/projects/4/env/bin/gunicorn --workers 3 --bind unix:/run/gunicorn.sock backend_settings.wsgi:application
ExecReload=/bin/kill -s HUP $MAINPID
KillMode=mixed
TimeoutStopSec=5
PrivateTmp=true

[Install]
WantedBy=multi-user.target
</file>

sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable --now gunicorn.service
sudo systemctl daemon-reload
sudo systemctl restart gunicorn

# sudo systemctl status gunicorn.service
# sudo systemctl disable gunicorn
# sudo systemctl stop gunicorn





sudo nano /etc/nginx/sites-available/192-168-80-130-http.conf
<file>
server {
listen 80;
listen [::]:80;

server_name localhost 127.0.0.1 192.168.80.130;

root /home/bogdan/projects/4;

location /.well-known/acme-challenge/ {}

location /favicon.ico {
    alias /home/bogdan/projects/4/static/logo.png;

    access_log off; log_not_found off;

    expires max;
}

location /robots.txt {
    alias /home/bogdan/projects/4/static/robots.txt;

    access_log off; log_not_found off;

    expires max;
}

location /static/ {
    alias /home/bogdan/projects/4/static/;

    expires max;
}

location /media/ {
    alias /home/bogdan/projects/4/static/media/;

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


sudo ln -s /etc/nginx/sites-available/192-168-80-130-http.conf /etc/nginx/sites-enabled/192-168-80-130-http.conf
sudo service nginx start
# sudo systemctl status nginx.service
# sudo ufw allow 443
# sudo ufw allow 8000
sudo ufw allow 'Nginx Full'
sudo systemctl reload nginx.service
# sudo nginx -t

sudo reboot

STATIC_URL = '/static/'
STATIC_ROOT = Path(BASE_DIR / 'static')
STATIC_DIR = Path(BASE_DIR / 'static')
STATICFILES_DIRS = [
    Path(BASE_DIR / 'static_external'),
    # Path(BASE_DIR / 'static')
]

