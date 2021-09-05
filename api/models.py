from django.db import models
from django.db.models.base import Model

# Create your models here.
class Cart(models.Model):
    name = models.TextField()
    price = models.FloatField()
    quantity = models.FloatField()