from django.contrib import admin

# Register your models here.
from .models import Payment
class Payment_admin(admin.ModelAdmin):
    list_display = ("amount", "method", "payment_status", "payment_date")

admin.site.register(Payment,Payment_admin)
