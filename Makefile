all: make_migrations run

APPNAME=baslerbauer_main
PIP=.virtualenv/bin/pip
PYTHON=.virtualenv/bin/python
MANAGE=${PYTHON} baslerbauer_site/manage.py

install: setup migrate sync

setup:
	virtualenv -p python3 .virtualenv
	${PIP} install -r requirements.txt

migrate:
	${MANAGE} migrate

make_migrations:
	${MANAGE} makemigrations ${APPNAME}

sync:
	${MANAGE} syncopenfarms

createsuperuser:
	${MANAGE} createsuperuser

run: migrate
	${MANAGE} collectstatic --no-input -l
	${MANAGE} runserver



