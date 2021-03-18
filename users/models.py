from django.contrib.auth.models import User
from django.db import models



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name="profile")
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100)
    image = models.ImageField(default="profileImages/defaultImg.jpg", upload_to="profileImages")

    def __str__(self):
        return f"{self.user}"