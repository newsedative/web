from django.contrib import admin
from .models import Auto, CarPart, Country

# Register your models here.

admin.site.register(Auto)
admin.site.register(CarPart)
admin.site.register(Country)