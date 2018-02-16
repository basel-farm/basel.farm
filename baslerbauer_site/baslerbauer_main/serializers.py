from rest_framework import serializers
from .models import Producer, Product, Stock

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = ('pk', 'openfarms_id', 'openfarms_url')
        read_only_fields = fields

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('pk', 'openfarms_id', 'openfarms_url')
        read_only_fields = fields

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('producer_openfarms_url', 'product_openfarms_url', 'amount')
        read_only_fields = fields
