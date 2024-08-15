from rest_framework import serializers

from .models import CartItems

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = ['id','product','quantity']