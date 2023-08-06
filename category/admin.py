from django.contrib import admin

# Register your models here.
from .models import Category

class Items_category(admin.ModelAdmin):
    list_display=["category"]
     
admin.site.register(Category,Items_category)