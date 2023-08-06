from django.contrib import admin


# Register your models here.

from .models import Product
class Product_admin(admin.ModelAdmin):
    list_display = ("name","stock","price","date_created","date_updated")
admin.site.register(Product,Product_admin)
