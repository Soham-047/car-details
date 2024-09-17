from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['username', 'car_company', 'car_name', 'car_desc'] 