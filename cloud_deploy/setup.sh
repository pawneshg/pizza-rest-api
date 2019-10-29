#!/usr/bin/env bash

set -e

PROJECT_GIT_URL='https://github.com/pawneshg/pizza-rest-api.git'
# store project location
PROJECT_BASE_PATH='/usr/local/apps/pizza-rest-api'

echo "Installing dependencies..."
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
sudo locale-gen en_US.UTF-8
sudo update-locale LANG=en_US.UTF-8
apt-get update
sudo apt-get install -y python3-dev sqlite python-pip python3-pip supervisor nginx git
sudo apt-get install -y python3-virtualenv

echo "Installed dependencies.."
# Create project directory
mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH

# Create virtual environment
mkdir -p $PROJECT_BASE_PATH/env
sudo python3 -m virtualenv $PROJECT_BASE_PATH/env

# Install python packages
$PROJECT_BASE_PATH/env/bin/pip install -r $PROJECT_BASE_PATH/requirements.txt
$PROJECT_BASE_PATH/env/bin/pip install uwsgi==2.0.18

# Run migrations and collectstatic
cd $PROJECT_BASE_PATH
$PROJECT_BASE_PATH/env/bin/python manage.py migrate
$PROJECT_BASE_PATH/env/bin/python manage.py collectstatic --noinput

# Configure supervisor
cp $PROJECT_BASE_PATH/cloud_deploy/supervisor_pizza_api.conf /etc/supervisor/conf.d/pizza_api.conf
supervisorctl reread
supervisorctl update
supervisorctl restart pizza_api

# Configure nginx
cp $PROJECT_BASE_PATH/cloud_deploy/nginx_pizza_api.conf /etc/nginx/sites-available/pizza_api.conf
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/pizza_api.conf /etc/nginx/sites-enabled/pizza_api.conf
systemctl restart nginx.service

echo "DONE! :)"
