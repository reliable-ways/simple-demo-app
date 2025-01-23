setup:
	@pyenv virtualenv 3.11 .venv

code:
	source .venv/bin/activate
	@pyenv shell 3.11

migrations:
	@python manage.py makemigrations
	@python manage.py migrate

run:
	@python manage.py runserver

user: 
	@python manage.py createsuperuser

build:
	@docker-compose build

run-docker:
	@docker-compose up