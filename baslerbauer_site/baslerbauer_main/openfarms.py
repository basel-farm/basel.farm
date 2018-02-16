#!/usr/bin/env python

import requests

# Helper classes to connect to openfarms

OPENFARMS_API = 'http://f.datalets.ch/api/v2/'

OPENFARMS_URLS = {
    'farms': OPENFARMS_API + 'farms/',
    'produce': OPENFARMS_API + 'produce/'
}

def list_items(url):
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    return data['items']

def list_farms():
    return list_items(OPENFARMS_URLS['farms'])

def list_produce():
    return list_items(OPENFARMS_URLS['produce'])
    

# DEBUG
if __name__=="__main__":
    print(list_farms())
    print(list_produce())

