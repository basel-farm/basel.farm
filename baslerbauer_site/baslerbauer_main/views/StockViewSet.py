from django.shortcuts import get_object_or_404
from baslerbauer_main.serializers import *
from rest_framework import viewsets
from rest_framework.response import Response


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

