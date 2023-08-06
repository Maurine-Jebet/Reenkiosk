from django.db import models

# Create your models here.
class Buyer(models.Model):
    first_name=models.CharField(max_length=20)
    second_name=models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=18)

