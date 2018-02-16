from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login as django_login
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from baslerbauer_main.models import Producer

# Create your views here.

class StockViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving stock.
    """
    def list(self, request):
        queryset = Stock.objects.all()
        serializer = StockSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Stock.objects.all()
        stock = get_object_or_404(queryset, pk=pk)
        serializer = StockSerializer(stock)
        return Response(serializer.data)
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

@csrf_exempt
def register(request):
        @csrf_protect
        def user_register(request):
            user = User.objects.create_user(username=request.POST.get("email"),password=request.POST.get("password"));
            p = Producer.objects.get(pk=request.POST.get("producer"))
            p.user=user
            p.save()
            return HttpResponse("Registered")
        if request.method == 'POST':
            return user_register(request)
        else:
            template = loader.get_template('baslerbauer_main/register.html')
            context = {
                'producer_list': Producer.objects.all()
            }
            return HttpResponse(template.render(context, request))
