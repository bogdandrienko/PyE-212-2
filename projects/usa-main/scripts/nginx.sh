# TODO NGINX ###########################################################################################################

# todo install
sudo apt-get update -y
sudo apt-get install -y nginx
# todo install

sudo usermod -aG user www-data






sudo nano /etc/nginx/sites-available/web-ilusa-kz-http.conf
#<file>
server {
listen 80;
listen [::]:80;

server_name web.ilusa.kz www.web.ilusa.kz;

root /home/ubuntu/web;

location /.well-known/acme-challenge/ {}

location /favicon.ico {
    alias /home/ubuntu/web/static/logo.png;

    access_log off; log_not_found off;

    expires max;
}

location /robots.txt {
    alias /home/ubuntu/web/static/robots.txt;

    access_log off; log_not_found off;

    expires max;
}

location /static/ {
    alias /home/bogdan/web/static/;

    expires max;
}

location /media/ {
    alias /home/ubuntu/web/static/media/;

    expires max;
}

location / {
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header Host $http_host;
    proxy_redirect off;
    proxy_buffering off;
    proxy_pass http://unix:/run/gunicorn.sock;
}
}
#</file>

sudo ln -s /etc/nginx/sites-available/web-ilusa-kz-http.conf /etc/nginx/sites-enabled/web-ilusa-kz-http.conf
sudo service nginx start
sudo systemctl status nginx.service
sudo ufw allow 'Nginx Full'
sudo systemctl reload nginx.service

sudo mv /etc/nginx/sites-available/web-ilusa-kz-http.conf /etc/nginx/sites-available/web.ilusa.kz-https.conf
sudo nano /etc/nginx/sites-available/web-ilusa-kz-http.conf
#<file>
server {
listen 80;
listen [::]:80;

server_name web.ilusa.kz www.web.ilusa.kz;

root /home/ubuntu/web;

location /.well-known/acme-challenge/ {}

location / {
    return 301 https://$server_name$request_uri;
}
}
#</file>

sudo certbot certonly --webroot -w /home/ubuntu/web -d web.ilusa.kz -m temiros@mail.ru --agree-tos
sudo openssl dhparam -out /etc/nginx/dhparam.pem 2048

sudo nano /etc/nginx/sites-available/web-ilusa-kz-https.conf
#<file>
server {
listen 443 ssl http2;
listen [::]:443 ssl http2;

ssl_certificate /etc/letsencrypt/live/web.ilusa.kz/fullchain.pem;
ssl_certificate_key /etc/letsencrypt/live/web.ilusa.kz/privkey.pem;

ssl_session_timeout 1d;
ssl_session_cache shared:MozSSL:10m;

ssl_dhparam /etc/nginx/dhparam.pem;

ssl_protocols TLSv1.2;
ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384;
ssl_prefer_server_ciphers off;

ssl_stapling on;
ssl_stapling_verify on;

ssl_trusted_certificate /etc/letsencrypt/live/web.ilusa.kz/chain.pem;

resolver 1.1.1.1;

client_max_body_size 30M;

server_name web.ilusa.kz www.web.ilusa.kz;

root /home/ubuntu/web;

location /.well-known/acme-challenge/ {}

location /favicon.ico {
    alias /home/ubuntu/web/static/logo.png;

    access_log off; log_not_found off;

    expires max;
}

location /robots.txt {
    alias /home/ubuntu/web/static/robots.txt;

    access_log off; log_not_found off;

    expires max;
}

location /static/ {
    alias /home/ubuntu/web/static/;

    expires max;
}

location /media/ {
    alias /home/ubuntu/web/static/media/;

    expires max;
}

location / {
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header Host $http_host;
    proxy_redirect off;
    proxy_buffering off;
    proxy_pass http://unix:/run/gunicorn.sock;
}
}
#</file>

sudo ln -s /etc/nginx/sites-available/web-ilusa-kz-https.conf /etc/nginx/sites-enabled/web-ilusa-kz-https.conf
sudo service nginx start
sudo systemctl status nginx.service
sudo ufw allow 'Nginx Full'
sudo systemctl reload nginx.service

# TODO NGINX ###########################################################################################################





#1 версия

# настройка nginx
# sudo nano /etc/nginx/sites-available/192.168.1.83-http.conf 
sudo nano /etc/nginx/sites-available/web-ilusa-kz-http.conf 
#<file>
server {
listen 80;
listen [::]:80;

#server_name localhost 127.0.0.1 192.168.1.83;  
server_name web.ilusa.kz www.web.ilusa.kz;   


#root /home/ubuntu/projects/mytodolist;
root /home/ubuntu/web;
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
#</file>

# sudo ln -s /etc/nginx/sites-available/192.168.1.83-http.conf /etc/nginx/sites-enabled/192.168.1.83-http.conf
sudo ln -s /etc/nginx/sites-available/web-ilusa-kz-http.conf /etc/nginx/sites-enabled/web-ilusa-kz-http.conf
sudo service nginx start
# sudo systemctl status nginx.service
# sudo ufw allow 443
# sudo ufw allow 8000
sudo ufw allow 'Nginx Full'
sudo systemctl reload nginx.service
#последний этап
# sudo nginx -t

sudo reboot