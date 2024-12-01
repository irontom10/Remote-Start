sudo apt update
sudo apt install nginx php-fpm php-cli python3-rpi.gpio


sudo rm /etc/nginx/sites-available/default
sudo cp ./files/nginx/default /etc/nginx/sites-available/default
sudo systemctl restart nginx

sudo cp -r ./files/website/* /var/www/html

sudo chmod -R 777 /var/www/html/
sudo chown -R www-data:www-data /var/www/html/
sudo chmod +x /var/www/html/remote_start.py
