sudo apt-get install postgresql

sudo -u postgres psql

\password

#Jap....

\q 

sudo nano /etc/postgresql/12/main/postgresql.conf

#в файле
    listen_adresses = '*'
#в файле


sudo nano /etc/postgresql/12/main/pg_hba.conf

#в файле
    host all all 0.0.0.0 0.0.0.0 md5
#в файле
sudo /etc/init.d/postgresql restart


sudo apt install firewalld

sudo firewall-cmd --permanent --add-port=5432/tcp

sudo systemctl reload firewalld

ip a

# теперь pg admin ip вставляем новый сервер и готово

# не забыть в .env поменять настройки для посгрес