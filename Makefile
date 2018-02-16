all: run

PIP=.virtualenv/bin/pip
PYTHON=.virtualenv/bin/python
MANAGE=${PYTHON} baslerbauer_site/manage.py

install:
	virtualenv .virtualenv
	${PIP} install -r requirements.txt

run:
	${MANAGE} migrate
	${MANAGE} runserver



