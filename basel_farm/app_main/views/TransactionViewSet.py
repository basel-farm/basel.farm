from django.db import transaction
from django.shortcuts import get_object_or_404
from django.db.models import F
from rest_framework import viewsets
from rest_framework.response import Response
from app_main.models import *
from app_main.serializers import TransactionSerializer
from datetime import datetime
import json

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
    
    @transaction.atomic
    def get_group_value(self):
        group = TransactionGroupCounter.objects.select_for_update().first()
        group.value += 1
        group.save()

        return group.value

    @transaction.atomic
    def update_stock(self, transactions):
        for t in transactions: 
            Stock.objects.filter( producer=t.producer
                                , product=t.product).update(amount=F('amount') - t.amount)
            t.save() 

    def create(self, request):
        consumer = request.user.consumer
        i = json.loads(request.body.decode('utf8'))
        trxs = []
        group = self.get_group_value()
        for e in i:
            producer = get_object_or_404( Producer.objects.all()
                                        , openfarms_id=e['producer_openfarms_id'])
            product = get_object_or_404( Product.objects.all()
                                       , openfarms_id=e['product_openfarms_id'])
            amount = e['amount']
            trxs.append(Transaction( group=group
                                   , date_time=datetime.now()
                                   , producer=producer
                                   , consumer=consumer
                                   , product=product
                                   , amount=amount
                                   ))
        self.update_stock(trxs)
        trx = Transaction.objects.all().filter(group=group)
        serializer = TransactionSerializer(trx, many=True)
        return Response(serializer.data)

