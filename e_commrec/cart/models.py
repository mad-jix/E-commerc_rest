from django.db import models

from product.models import Products
from user.models import Customer

# Create your models here.
class CartItems(models.Model):
    product=models.ForeignKey(Products,related_name='addtocart',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='cartitems')