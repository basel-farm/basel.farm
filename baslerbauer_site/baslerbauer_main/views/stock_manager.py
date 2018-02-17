from .utils import HttpOpenFarmsResponse
from django.shortcuts import redirect
from django.template import loader


def stock_manager(request):
    if request.user.is_authenticated:
        template = loader.get_template('baslerbauer_main/stock_manager.html')
        context = { }
        return HttpOpenFarmsResponse(template.render(context,request))
    else:
        return redirect('../login/')

