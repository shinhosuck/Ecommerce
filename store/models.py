from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db import models
from PIL import Image 

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
        return f"{self.name_name}"


class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    class Meta:
            verbose_name_plural = "Sub Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    sub_category = models.OneToOneField(SubCategory, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    image = models.ImageField(default="productImages/defaultProductImage.jpg", upload_to="productImages")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    on_stock = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.width > 400 or img.height > 400:
            new_img = (400, 400)
            img.thumbnail(new_img)
            img.save(self.image.path)

    def __str__(self):
        return self.product_name