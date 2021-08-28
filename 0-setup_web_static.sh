#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static
sudo apt-get update -y
sudo apt-get install -y nginx
sudo chown -R ubuntu:ubuntu /data/
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
sudo echo "Holberton School" > /data/web_static/releases/test/index.html
ln -s -f /data/web_static/releases/test/ /data/web_static/current
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
