
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Restaurant(models.Model):
    restaurantName = models.CharField(max_length=50)
    address = models.TextField()
    restaurantContact = PhoneNumberField()
    email = models.EmailField()
    password = models.CharField(max_length=30)
