from rest_framework import serializers
from .models import Transaction, Stock

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ( 'producer_openfarms_id'
                 , 'producer_openfarms_url'
                 , 'product_openfarms_id'
                 , 'product_openfarms_url'
                 , 'amount'
                 )
        read_only_fields = fields

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ( 'group'
                 , 'date_time'
                 , 'producer_openfarms_id'
                 , 'consumer'
                 , 'product_openfarms_id'
                 , 'amount'
                 )
        read_only_fields = fields
