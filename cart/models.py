from django.db import models

# Create your models here.

from inventory.models import Product
# Create your models here.
class Cart(models.Model):
    products = models.ManyToManyField(Product)
    product = models.CharField(max_length=30)
    quantity = models.PositiveIntegerField()
