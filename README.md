# Crops and Markets

An utterly fantastic project for the agricultural industry, developed using Django 1.8, and my thesis.

## How to Use

To use this project, follow these steps:

1. Create your working environment.
2. Install Django
	`$ pip install django`
3. Deploy this code.
4. Load initial data
	`python manage.py loaddata crops_and_markets_app/fixtures/initial_data.json`
4. Run the server
	`$ python manage.py runserver`
5. Enjoy

## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise
- Enhancements to Django's database functionality via django-postgrespool and dj-database-url

## Further Reading

- [Semillas-SZ](http://www.semillas-sz.com/)
- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [django-postgrespool](https://warehouse.python.org/project/django-postgrespool/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
