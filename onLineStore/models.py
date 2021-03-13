from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Customer(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    email = models.CharField(max_length=200)
    quantity_ordered = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=100000, decimal_places=2)
    image = models.ImageField(default="product_images/default.jpg", upload_to="product_images")

    def __str__(self):
        return self.name



class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.customer}"


class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=100000, decimal_places=2, null=True)
    date_ordered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.customer} {self.product}"


class Order(models.Model):
    purchase= models.ForeignKey(Purchase, on_delete=models.SET_NULL, null=True)
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.SET_NULL, null=True)
    total = models.DecimalField(max_digits=100000, decimal_places=2)
    date_ordered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.shipping_address}"




