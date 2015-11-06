# Crops and Markets

An utterly fantastic project for the agricultural industry, developed using Django 1.8, and @bkupfer's thesis.

## How to Use

To use this project, follow these steps:

1. Create your working environment.
	It must have python 2.7 and pip installed.
2. Install python requirements
	`$ pip install -r requirements.txt`
	-- Note:
		- If in Windows must install Microsoft Visual C++ Compiler (http://www.microsoft.com/en-us/download/confirmation.aspx?id=44266)
		- Must install postrgresSQL (http://www.postgresql.org/download/)
3. Deploy $(this) code.
4. Create database
	`python manage.py migrate`
5. Load initial data
	- `$ python manage.py loaddata crops_and_markets_app/fixtures/initial_data.json`
	- `$ python manage.py loaddata crops_and_markets_app/fixtures/users.json`
	- `$ python manage.py loaddata crops_and_markets_app/fixtures/regions.json`
6. Run the server
	`$ python manage.py runserver 8000`
7. Enjoy

## Technical Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise
- Enhancements to Django's database functionality via django-postgrespool and dj-database-url

## Further Reading

- [Semillas-SZ](http://www.semillas-sz.com/)
- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [django-postgrespool](https://warehouse.python.org/project/django-postgrespool/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
