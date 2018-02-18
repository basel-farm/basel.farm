from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from app_main.models import Producer,Consumer
from django.shortcuts import redirect

@csrf_exempt
def register(request):
    @csrf_protect
    def user_register(request):
        user = User.objects.create_user(username=request.POST.get("email"),password=request.POST.get("password"));
        if request.POST.get("type") == "type_producer":
            p = Producer.objects.get(pk=request.POST.get("producer"))
            p.user=user
            p.save()
        elif request.POST.get("type")=="type_consumer":
            Consumer.objects.create(user=user)
        return redirect("login")
    if request.method == 'POST':
        return user_register(request)
    else:
        template = loader.get_template('app_main/register.html')
        context = {
            'producer_list': Producer.objects.all()
        }
        return HttpResponse(template.render(context, request))

