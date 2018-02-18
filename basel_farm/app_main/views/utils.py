from django.http import HttpResponse
from app_main.openfarms import OPENFARMS_DOMAIN

class HttpOpenFarmsResponse(HttpResponse):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['Access-Control-Allow-Methods'] =  "GET"
        self['Access-Control-Allow-Origin'] = OPENFARMS_DOMAIN

