#!/usr/bin/env python

import requests

# Helper classes to connect to openfarms

openfarms_api = 'http://f.datalets.ch/api/v2/'

openfarms_urls = {
    'farms': openfarms_api + 'farms/',
    'produce': openfarms_api + 'produce/'
}

def error(errstr):
    print(errstr)

def list_items(url):
    response = requests.get(url)
    if response.status_code != requests.codes.ok:
        error("There was an error sending the request: {}".format(response.status_code))
        return None

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

