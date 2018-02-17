from django.shortcuts import get_object_or_404
from baslerbauer_main.serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponse

class StockViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving stock.
    """
    def list(self, request):
        queryset = Stock.objects.all()
        username = self.request.query_params.get('own', None)
        if username is not None:
            queryset = queryset.filter(producer=request.user.producer)
        serializer = StockSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Stock.objects.all()
        stock = get_object_or_404(queryset, pk=pk)
        serializer = StockSerializer(stock)
        return Response(serializer.data)
    
    def create(self, request):
        if not hasattr(request.user,'producer'):
            return HttpResponse('Unauthorized', status=403)
        producer = request.user.producer
        product_openfarms_id = request.POST.get("product_id")
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

