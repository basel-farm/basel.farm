from django.db import models
from .openfarms import OPENFARMS_URLS
from django.contrib.auth.models import User

# c.f: https://docs.djangoproject.com/en/2.0/ref/models/fields/#model-field-types

class Producer(models.Model):
    openfarms_id = models.PositiveIntegerField()
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True,default=None)

    @classmethod
    def from_openfarms(cls, data):
        """Convert a OpenFarms JSON farm objects to a Producer model instance
        
           This is used by the syncopenfarms command to create producers"""
        return cls(openfarms_id=data['id'])

    @property
    def openfarms_url(self):
        return "{}{}/".format(OPENFARMS_URLS['farms'](), self.openfarms_id)

    def __str__(self):
        return "Producer {}".format(self.openfarms_id)

class Consumer(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True,default=None)

class Product(models.Model):
    openfarms_id = models.PositiveIntegerField()

    @property
    def openfarms_url(self):
        return "{}{}/".format(OPENFARMS_URLS['produce'](), self.openfarms_id)

    @classmethod
    def from_openfarms(cls, data):
        """Convert a OpenFarms JSON produce objects to a Product model instance
        
           This is used by the syncopenfarms command to create products"""
        return cls(openfarms_id=data['id'])

    def __str__(self):
        return "Product {}".format(self.openfarms_id)
    
class Stock(models.Model):
    producer = models.ForeignKey(Producer, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    amount = models.IntegerField()

    @property
    def producer_openfarms_url(self):
        return self.producer.openfarms_url

    @property
    def producer_openfarms_id(self):
        return self.producer.openfarms_id

    @property
    def product_openfarms_url(self):
        return self.product.openfarms_url

    @property
    def product_openfarms_id(self):
        return self.product.openfarms_id


class Transaction(models.Model):
    group = models.PositiveIntegerField()
    date_time = models.DateTimeField()
    producer = models.ForeignKey(Producer, on_delete=models.PROTECT)
    consumer = models.ForeignKey(Consumer, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    amount = models.IntegerField()

    @property
    def producer_openfarms_id(self):
        return self.producer.openfarms_id

    @property
    def product_openfarms_id(self):
        return self.product.openfarms_id

class TransactionGroupCounter(models.Model):
    value = models.PositiveIntegerField()

