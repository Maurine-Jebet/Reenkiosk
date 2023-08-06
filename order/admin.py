from django.contrib import admin

# Register your models here.
from .models import Order
class Order_admin(admin.ModelAdmin):
    list_display = ("date_ordered", "complete", "transaction_id")
admin.site.register(Order,Order_admin)