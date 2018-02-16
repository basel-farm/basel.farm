all: make_migrations run

APPNAME=baslerbauer_main
PIP=.virtualenv/bin/pip
PYTHON=.virtualenv/bin/python
MANAGE=${PYTHON} baslerbauer_site/manage.py

install:
	virtualenv .virtualenv
	${PIP} install -r requirements.txt

make_migrations:
	${MANAGE} makemigrations ${APPNAME}

sync:
	${MANAGE} syncopenfarms

run:
	${MANAGE} migrate
	${MANAGE} collectstatic --no-input -l
	${MANAGE} runserver



