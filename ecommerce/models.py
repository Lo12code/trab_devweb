from django.db import models
from django.contrib.auth.models import User # new

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    quantity = models.IntegerField()

class User(models.Model):
    name = models.CharField(max_length=200)

class Cart(models.Model):

    cart_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
