from django.db import models

# Create your models here.
from customer.models import Buyer
from cart.models import Cart
from delivery.models import Delivery

class Order(models.Model):
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100)
    customer = models.ForeignKey(Buyer,null=True,on_delete = models.CASCADE)
    cart = models.ForeignKey(Cart,null=True,on_delete=models.CASCADE)
    delivery = models.OneToOneField(Delivery,null=True,on_delete=models.CASCADE)
