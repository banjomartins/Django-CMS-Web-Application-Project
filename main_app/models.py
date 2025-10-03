from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# User Information
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    hobby = models.CharField(max_length=100)
    favorite_food = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.city}"

# Product Information
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    photo = models.ImageField(upload_to="product_photos/", blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({'Available' if self.is_available else 'Unavailable'})"