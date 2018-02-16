all: run

PIP=.virtualenv/bin/pip
PYTHON=.virtualenv/bin/python

install:
	virtualenv .virtualenv
	${PIP} install -r requirements.txt

run:
	${PYTHON} baslerbauer_site/manage.py runserver



