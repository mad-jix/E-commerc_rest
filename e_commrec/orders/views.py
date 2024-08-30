from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer
from cart.models import CartItems
from user.models import Customer

class OrderCreateView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        cart_item_id = request.data.get('cart_item_id')
        owner_id = request.data.get('owner_id')
        
        try:
            cart_item = CartItems.objects.get(id=cart_item_id)
            owner = Customer.objects.get(id=owner_id)
        except CartItems.DoesNotExist:
            return Response({"error": "Cart item not found"}, status=status.HTTP_404_NOT_FOUND)
        except Customer.DoesNotExist:
            return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)
        
        order = Order.objects.get(
            orderstatus=Order.ORDER_PROCESSED,
            owner=owner,
            product=cart_item
        )
        
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


