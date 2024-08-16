from django.shortcuts import get_object_or_404

from rest_framework import generics, status, permissions
from rest_framework.response import Response

from .models import CartItems
from .serializers import CartItemSerializer
from product.models import Products
from user.models import Customer

class CartView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        user = request.user
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        # Check if the user is authenticated
        if not user.is_authenticated:
            return Response({"detail": "Authentication required to add items to the cart."}, status=status.HTTP_401_UNAUTHORIZED)

        # Get or create the customer profile
        customer, created = Customer.objects.get_or_create(user=user)

        # Get the product
        product = get_object_or_404(Products, id=product_id)

        # Create or update the cart item
        cart_item, created = CartItems.objects.get_or_create(user=customer, product=product)
        if not created:
            cart_item.quantity += int(quantity)
        else:
            cart_item.quantity = int(quantity)
        cart_item.save()

        # Serialize the response
        serializer = self.get_serializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)





