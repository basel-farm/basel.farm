from django.shortcuts import get_object_or_404
from app_main.serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseForbidden
from app_main.models import *

class StockViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving stock.
    """
    def list(self, request):
        queryset = Stock.objects.all()
        get_own = self.request.query_params.get('own', None)
        if get_own:
            if request.user.is_authenticated and request.user.producer:
                queryset = queryset.filter(producer=request.user.producer)
            else: # Wanted to see own, but is not producer. 403
                return HttpResponseForbidden("You are not a producer.")
        serializer = StockSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Stock.objects.all()
        stock = get_object_or_404(queryset, pk=pk)
        serializer = StockSerializer(stock)
        return Response(serializer.data)
    
    def create(self, request):
        if not self.user.is_authenticated or not request.user.producer:
            return HttpResponseForbidden('You must be a producer to do this.')
        producer = request.user.producer
        product_openfarms_id = request.POST.get("product_openfarms_id")
        product = get_object_or_404(Product.objects.all(), openfarms_id=product_openfarms_id)
        amount = request.POST.get("amount")
        try:
            stock = Stock.objects.get(producer=producer, product=product)
            stock.amount += int(amount)
            stock.save()
        except Stock.DoesNotExist:
            stock = Stock.objects.create(producer=producer, product=product, amount=amount)
        serializer = StockSerializer(stock)
        return Response(serializer.data)

