from django.contrib import admin

# Register your models here.
from .models import Vendor
class Vendor_admin(admin.ModelAdmin):
    list_display = ("first_name","last_name","email","phone","password")
admin.site.register(Vendor,Vendor_admin)