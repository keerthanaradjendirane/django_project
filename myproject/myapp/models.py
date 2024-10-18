from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)  # Add this field
    phone_number = models.CharField(max_length=15)  # Add this field
