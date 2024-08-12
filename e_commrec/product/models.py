from django.db import models

# Create your models here.

class Products(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'live'),(DELETE,'delete'))
    AVAILABLE = 1
    NOT_AVAILABLE = 0
    STOCK_CHOICES = (
        (AVAILABLE, 'Product available'),
        (NOT_AVAILABLE, 'Product not available'))
    name=models.CharField(max_length=30)
    price =models.FloatField(default=0)
    description=models.TextField(default=0)
    stock = models.IntegerField(choices=STOCK_CHOICES, default=AVAILABLE)
# Part 2.2 Product image model
    image=models.ImageField(upload_to='media/')
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)

    def __str__(self) -> str:
        return self.name