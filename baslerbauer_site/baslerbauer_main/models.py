from django.db import models

# c.f: https://docs.djangoproject.com/en/2.0/ref/models/fields/#model-field-types

class Producer(models.Model):
    open_farms_url = models.URLField()

class Consumer(models.Model):
    pass

class Product(models.Model):
    open_farms_url = models.URLField()

class Stock(models.Model):
    producer = models.ForeignKey( Producer
                                , on_delete=models.PROTECT
                                )
    product = models.ForeignKey( Product
                               , on_delete=models.PROTECT
                               )
    amount = models.IntegerField()

    def producer_url(self):
        return self.producer.open_farms_url

    def product_url(self):
        return self.product.open_farms_url

class Transaction(models.Model):
    group = models.PositiveIntegerField()
    date_time = models.DateTimeField()
    producer = models.ForeignKey( Producer
                                , on_delete=models.PROTECT
                                )
    consumer = models.ForeignKey( Consumer
                                , on_delete=models.PROTECT
                                )
    product = models.ForeignKey( Product
                               , on_delete=models.PROTECT
                               )
    amount = models.IntegerField()
