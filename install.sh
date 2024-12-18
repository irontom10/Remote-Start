sudo apt update
sudo apt install nginx php-fpm php-cli python3-rpi.gpio


sudo rm /etc/nginx/sites-available/default
sudo cp ./files/nginx/default /etc/nginx/sites-available/default
sudo systemctl restart nginx

sudo cp -r ./files/website/* /var/www/html

sudo chmod -R 777 /var/www/html/
sudo chown -R www-data:www-data /var/www/html/

sudo rm /etc/systemd/system/remote_start.service
sudo cp ./files/systemctl/remote_start.service /etc/systemd/system/remote_start.service
sudo chmod 644 /etc/systemd/system/remote_start.service
sudo systemctl daemon-reload
sudo cp ./files/www-data /etc/sudoers.d/www-data
sudo chmod 440 /etc/sudoers.d/www-data

sudo rm -rf /usr/local/bin/remote_start/
sudo mkdir /usr/local/bin/remote_start/
sudo cp -R ./files/remote_start/ /usr/local/bin/
sudo chmod +x /usr/local/bin/remote_start/*
sudo chmod 777 /var/log/remote_start.log