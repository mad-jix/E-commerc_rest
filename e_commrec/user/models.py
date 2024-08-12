from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Coustomer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    name= models.CharField(max_length=10)
    email = models.EmailField()
    