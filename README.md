# SeqUDAS Web

## Setting up a Development Environment

Set an environment variable to use as a Django `SECRET_KEY`. You can use [this site](https://www.miniwebtool.com/django-secret-key-generator/):

```
export DJANGO_SECRET_KEY=yoursecretkey
```

### Create the base Django datbase tables

```
docker-compose run web python /code/manage.py migrate --noinput
```

### Create a Django admin user

```
docker-compose run web python manage.py createsuperuser
```

Follow the prompts to enter username and password for the Django admin user.

### Create sequdas database tables and load seed data for testing/development.
```
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
docker-compose run web python manage.py loaddata seed_data
```