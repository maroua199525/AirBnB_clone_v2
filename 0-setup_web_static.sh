#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static
sudo apt-get update -y
sudo apt-get install -y nginx
sudo chown -R ubuntu:ubuntu /data/
sudo chmod -R 755 /var/www
sudo echo "Holberton School" > /data/web_static/releases/test/index.html
if (!file_exists('/data/')) {
    mkdir('/data/', 0777, true);
}
if (!file_exists('/data/web_static/')) {
    mkdir('/data/web_static/', 0777, true);
}
if (!file_exists('/data/web_static/releases/')) {
    mkdir('/data/web_static/releases/', 0777, true);
}
if (!file_exists('/data/web_static/shared/')) {
    mkdir('/data/web_static/shared/', 0777, true);
}
if (!file_exists('/data/web_static/releases/test/')) {
    mkdir('/data/web_static/releases/test/', 0777, true);
}
ln -s -f /data/web_static/releases/test/ /data/web_static/current
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
