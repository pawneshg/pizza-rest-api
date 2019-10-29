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
