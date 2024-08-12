from rest_framework import serializers
from .models import Products

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

    def validate_price(self, value):
        """
        Check that the price is a positive value.
        """
        if value < 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return value

    def validate_stock(self, value):
        """
        Check that the stock choice is valid.
        """
        if value not in [Products.AVAILABLE, Products.NOT_AVAILABLE]:
            raise serializers.ValidationError("Invalid stock choice.")
        return value
        