from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login as django_login
from django.views.decorators.csrf import csrf_exempt, csrf_protect


@csrf_exempt
def login(request):
    @csrf_protect
    def user_login(request):
        user = authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
        if user is not None:
            django_login(request, user)
            return HttpResponse("OK")
        else:
            return HttpResponse("FALSE")
    if request.method == 'POST':
        return user_login(request)
    else:
        template = loader.get_template('baslerbauer_main/login.html')
        context = {
        }
        return HttpResponse(template.render(context, request))
