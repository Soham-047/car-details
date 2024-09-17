from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ('username', 'car_company', 'car_name', 'car_desc')  # Display these fields in the list view
    fields = ('username', 'car_company', 'car_name', 'car_desc')  # Display these fields in the form view

admin.site.register(Car, CarAdmin)
