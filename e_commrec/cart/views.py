from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions

from .models import CartItems
from .serializers import CartItemSerializer
from product.models import Products
from user.models import Customer

class CartView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        # Get or create the customer profile (assuming user is authenticated)
        customer = get_object_or_404(Customer, user=user)

        # Get the product
        product = get_object_or_404(Products, id=product_id)

        # Create or update the cart item
        cart_item, created = CartItems.objects.get_or_create(owner=customer, product=product)
        if not created:
            cart_item.quantity += int(quantity)
        else:
            cart_item.quantity = int(quantity)
        cart_item.save()

        # Serialize the response
        serializer = self.get_serializer(cart_item)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)




