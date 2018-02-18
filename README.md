# basel.farm
Website: https://basel.farm

Open Food Hackdays Feb 2018: https://hack.opendata.ch/project/174

# Setup
You will need to
* Install virtualenv and requirements
* Migrate database changes and collect static content
* Sync farms and produces with openfarms
* Run local development instance

## Using make
```bash
$ make install
$ make sync
$ make createsuperuser # optional: creates an admin user
$ make run
```

## Using manage.py
```bash
$ virtualenv .virtualenv
$ .virtualenv/bin/pip install -r requirements.txt
$ .virtualenv/bin/python basel_farm/manage.py migrate
$ .virtualenv/bin/python basel_farm/manage.py createsuperuser
$ .virtualenv/bin/python basel_farm/manage.py syncopenfarms
$ .virtualenv/bin/python basel_farm/manage.py collectstatic
$ .virtualenv/bin/python basel_farm/manage.py runserver
```
