from django.contrib.auth.models import User
from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=100000, decimal_places=2)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to="product_images")

    def __str__(self):
        return self.name 