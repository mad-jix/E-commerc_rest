from django.db import models

from user.models import Customer
from cart.models import CartItems

class Order(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = (
        (LIVE, 'live'),
        (DELETE, 'delete')
    )
    
    CART_STAGE = 0
    ORDER_PROCESSED = 1
    DELIVERED = 2
    REJECTED = 3
    STATUS_CHOICE = (
        (CART_STAGE, "CART_STAGE"),
        (ORDER_PROCESSED, "ORDER_PROCESSED"),
        (DELIVERED, "DELIVERED"),
        (REJECTED, "REJECTED")
    )
    
    orderstatus = models.IntegerField(choices=STATUS_CHOICE, default=CART_STAGE)
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='orders')
    product = models.ForeignKey(CartItems, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"orders-{self.id}-{self.owner}"
