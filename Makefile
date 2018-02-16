all: run


install:
	virtualenv .virtualenv
	.virtualenv/bin/pip install -r requirements.txt

run:



