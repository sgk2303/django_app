from django.contrib import admin
from .models import Site, IAP, switch, Order
# Register your models here.

admin.site.register(Site)
admin.site.register(IAP)
admin.site.register(switch)
admin.site.register(Order)