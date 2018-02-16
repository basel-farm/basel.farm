#!/usr/bin/env python

import requests

# Helper classes to connect to openfarms

openfarms_api = 'http://f.datalets.ch/api/v2/'

openfarms_urls = {
    'farms': openfarms_api + 'farms/',
    'produce': openfarms_api + 'produce/'
}

def list_items(url):
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    return data['items']

def list_farms():
    return list_items(openfarms_urls['farms'])

def list_produce():
    return list_items(openfarms_urls['produce'])
    

# DEBUG
if __name__=="__main__":
    print(list_farms())
    print(list_produce())

