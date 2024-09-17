# models.py
from django.db import models

class Car(models.Model):
    username = models.CharField(max_length=100)
    car_company = models.CharField(max_length=100)
    car_name = models.CharField(max_length=100)
    car_desc = models.TextField()

    def __str__(self):
        return self.car_name
