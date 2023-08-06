from django.contrib import admin

# Register your models here.

from .models import Cart
class Cart_admin(admin.ModelAdmin):
    list_display = ["product","quantity"]
admin.site.register(Cart,Cart_admin)
