from django.db import models

# c.f: https://docs.djangoproject.com/en/2.0/ref/models/fields/#model-field-types

class Label(models.Model):
    name = models.CharField(max_length=120)

class Producer(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    labels = models.ManyToManyField(Label)
    description = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=120)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)

class Offer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    amount = models.IntegerField()

