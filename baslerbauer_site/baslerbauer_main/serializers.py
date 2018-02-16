from rest_framework import serializers
from .models import *

class ProducerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Producer
		fields = ('open_farms_url')
		read_only_fields = fields

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('open_farms_url')
		read_only_fields = fields

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('producer', 'product', 'amount')
        read_only_fields = fields
