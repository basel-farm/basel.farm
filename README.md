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

# API
There are the following APIs available:
* api/stock/
* api/transaction/

## api/stock/
Two operations are supported:
* GET: get the current products available on the stocks
* POST: add or remove a product from a stock of a specific producer

#### GET
Three different parameter combinations are supported:
* no paramter: get information for all producers and products
* query parameter 'own': get available products of the specified producer
* url parameter api/stock/{product_openfarm_id}/: get all producer who have the {product_openfarm_id} product on stock

#### POST
This operation updates the current stock information. The following parameters are required and must be provided in the standard HTML POST format:
* product_openfarms_id: land2door product identification 
* amount: positive (add) or negative (remove) number 

An authentication is required and the operation is available only for users registered as producers.

## api/transaction/
Two operations are supported
* GET: retrieve all transactions resgistered in the system
* POST: create a new transaction, i.e. order a list of products from specified producers

#### GET
Two different parameter combinations are supported:
* no paramter: get all registered transactions in the system
* query parameter 'own': get all transactions of the specified producer

#### POST
This operation accepts a list of transactions. Each transaction represents an order of a specific product from a specific producer. The information must be provided in the request body (in UTF-8 encoding) as an array of JSON objects with the following attributes:
* producer_openfarms_id: land2door producer identification
* product_openfarms_id: land2door product identification
* amount: a positive number representing the size of the order

An authentication is required and the operation is available only for users registered as consumers.

Example:
```
$ cat trx.json
[
    {
        "producer_openfarms_id": 1,
        "product_openfarms_id": 1,
        "amount": 2
    },
    {
        "producer_openfarms_id": 2,
        "product_openfarms_id": 2,
        "amount": 1
    }
]

$ curl -u 'username:password' --data-binary @trx.json -H "contentType: 'application/json'" http://127.0.0.1:8000/api/transaction/
[{"group":3,"date_time":"2018-02-19T19:05:37.008972Z","producer_openfarms_id":1,"consumer":1,"product_openfarms_id":1,"amount":2},{"group":3,"date_time":"2018-02-19T19:05:37.009913Z","producer_openfarms_id":2,"consumer":1,"product_openfarms_id":2,"amount":1}]
```

