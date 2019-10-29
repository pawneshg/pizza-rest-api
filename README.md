# Pizza REST API

Pizza Ordering REST API

# Packages Used.
- django ==2.2.4
- djangorestframework==3.9.2
- django-filter==0.15.3
- Postgres = 9.X

## Setup through Vagrant file
### Prerequiste
- Virtualbox . Dowload from https://www.virtualbox.org/wiki/Downloads
## Stepup command.
1. Clone the project from github
    ```git clone 'https://github.com/pawneshg/pizza-rest-api.git'```
2. From project directory start the vagrant.
    ```$vagrant up```
3. To login into the machine ```$vagrant ssh```
4. Execute following commands.
   ```
   cd /vagrant
   python -m venv ~/env
   source ~/env/bin/activate
   pip install -r requirements.txt
   
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver 0.0.0.0:8000
   ```
5. Login to browser: http://localhost:8000/api/


### Setup on EC2 Instance or Ubuntu Machine:
1. ssh machine ``$ssh root@1.0.0.0```
2. curl -sL https://raw.githubusercontent.com/pawneshg/pizza-rest-api/master/cloud_deploy/setup.sh | sudo bash -
3. Update the ALLOWED_HOST at https://github.com/pawneshg/pizza-rest-api/blob/master/pizza_project/settings.py#L28 by entering your public accessible host url.
4. Commit step3  changes to github or in your instance.
5. Goto Instance project location 
```
cd /usr/local/apps/pizza-rest-api
sudo sh ./cloud_deploy/update.sh
```
6. Optional: To create superuser
```
$sudo env/bin/python manage.py createsuperuser
```
7. Login to browser http:/{hostname}/api/
