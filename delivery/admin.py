from django.contrib import admin

# Register your models here.
from .models import Delivery
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ("order_name", "contact_number", "delivery_date", "delivery_time", "delivery_driver_name", "delivery_address", "delivery_status")
admin.site.register(Delivery, DeliveryAdmin)