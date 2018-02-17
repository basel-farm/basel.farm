from django.shortcuts import get_object_or_404
from baslerbauer_main.serializers import *
from rest_framework import viewsets
from rest_framework.response import Response


class TransactionViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for submitting a booking transaction
    """
    def list(self, request):
        queryset = Transaction.objects.all()
        username = self.request.query_params.get('own', None)
        if username is not None:
            queryset = queryset.filter(producer=request.user.producer)
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Transaction.objects.all()
        trx = get_object_or_404(queryset, pk=pk)
        serializer = TransactionSerializer(trx)
        return Response(serializer.data)
    
    def create(self, request):
        consumer = request.user.consumer
        producer_openfarms_id = request.POST.get("producer_openfarms_id")
        producer = get_object_or_404(Producer.objects.all(), openfarms_id=producer_openfarms_id)
        product_openfarms_id = request.POST.get("product_openfarms_id")
        product = get_object_or_404(Product.objects.all(), openfarms_id=product_openfarms_id)
        amount = request.POST.get("amount")
        trx = Transaction.objects.get( group=0
                                     , producer=producer
                                     , consumer=consumer
                                     , product=product
                                     , amount=amount
                                     )
        trx.save()
        serializer = TrnsactionSerializer(trx)
        return Response(serializer.data)
