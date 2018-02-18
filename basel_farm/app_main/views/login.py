from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login as django_login
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.shortcuts import redirect

@csrf_exempt
def login(request):
    @csrf_protect
    def user_login(request):
        user = authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
        if user is not None:
            django_login(request, user)
            return redirect('../stocks/')
        else:
            template = loader.get_template('baslerbauer_main/login.html')
            context = {
                'login_failed' : True
            }
            return HttpResponse(template.render(context, request))
    if request.method == 'POST':
        return user_login(request)
    else:
        template = loader.get_template('app_main/login.html')
        context = {
        }
        return HttpResponse(template.render(context, request))

