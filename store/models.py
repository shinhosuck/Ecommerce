from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db import models


class Customer(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name="customer")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    country = CountryField()


    def __str__(self):
        return f"{self.name}"

