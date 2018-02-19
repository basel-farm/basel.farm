from .utils import HttpOpenFarmsResponse
from . import login

from django.shortcuts import redirect
from django.template import loader


def stocks(request):
    template = loader.get_template('app_main/stocks.html')
    context = { }
    return HttpOpenFarmsResponse(template.render(context,request))
