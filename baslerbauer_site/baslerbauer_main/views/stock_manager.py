from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader


def stock_manager(request):
    if request.user.is_authenticated:
        template = loader.get_template('baslerbauer_main/stock_manager.html')
        context = { }
        return HttpResponse(template.render(context,request))
    else:
        redirect('login')

