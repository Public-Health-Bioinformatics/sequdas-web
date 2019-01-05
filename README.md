# SeqUDAS Web

## Setting up a Development Environment

Set an environment variable to use as a Django `SECRET_KEY`. You can use [this site](https://www.miniwebtool.com/django-secret-key-generator/):

```
export DJANGO_SECRET_KEY=yoursecretkey
```

### Build the Development Environment

```
docker-compose up -d --build
```

### Create the base Django datbase tables

```
docker-compose exec web python /code/manage.py migrate --noinput
```

### Create a Django admin user

```
docker-compose exec web python manage.py createsuperuser
```

Follow the prompts to enter username and password for the Django admin user.

### Create sequdas database tables and load seed data for testing/development.
```
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py loaddata users
docker-compose exec web python manage.py loaddata seed_data
```