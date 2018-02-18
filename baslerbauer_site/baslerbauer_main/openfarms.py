#!/usr/bin/env python

import requests

# Helper classes to connect to openfarms

OPENFARMS_DOMAIN = 'http://f.datalets.ch'
OPENFARMS_API = OPENFARMS_DOMAIN+'/api/v2/'

def url_with_offset(url):
    """A function which takes an url and returns an url builder. The url builder takes an offset"""
    def func(offset=0):
        if offset == 0:
            return url
        else:
            return url+'?offset={}'.format(offset)
    return func

OPENFARMS_URLS = {
    'farms': url_with_offset(OPENFARMS_API + 'farms/'),
    'produce': url_with_offset(OPENFARMS_API + 'produce/')
}

def get_json(url):
    response = requests.get(url)
    response.raise_for_status()

    return response.json()


def list_items(url_func):
    """url_func is a function which takes an offset and returns an url"""

    data = get_json(url_func(offset=0))

    # Check how many items there are
    total_count = data['meta']['total_count']
    limit = len(data['items'])

    return data['items'] + list_items_paginated(url_func, total_count, offset=limit)


def list_items_paginated(url_func, total_count, offset):
    if total_count <= offset:
        return []

    data = get_json(url_func(offset))
    limit = len(data['items'])

    return data['items'] + list_items_paginated(url_func, total_count, offset=offset+limit)


def list_farms():
    return list_items(OPENFARMS_URLS['farms'])

def list_produce():
    return list_items(OPENFARMS_URLS['produce'])
    

# DEBUG
if __name__=="__main__":
    print(list_farms())
    print(list_produce())

