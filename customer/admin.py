from django.contrib import admin

# Register your models here.
from.models import Buyer

class Buyer_admin(admin.ModelAdmin):
    list_display=("first_name","second_name","phone","email")

    
admin.site.register(Buyer,Buyer_admin)