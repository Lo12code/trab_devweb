from django.db import models
from django.contrib.auth.models import User # new

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.CharField(max_length=200, default='00,00')


class Cart(models.Model):

    cart_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    products = models.ManyToManyField(Product)