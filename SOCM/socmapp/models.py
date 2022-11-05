from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Appoinment(models.Model):
    name = models.CharField(max_length=50, blank=True)
    phone = PhoneNumberField(unique = True, null = False, blank = False)
    email = models.EmailField(blank=True)
    work = models.CharField(max_length=50, blank=True)
    date = models.DateField()
