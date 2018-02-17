from django.http import HttpResponse
from django.template import loader

def transactions(request):
    template = loader.get_template('baslerbauer_main/transactions.html')
    context = {
    }
    return HttpResponse(template.render(context, request))