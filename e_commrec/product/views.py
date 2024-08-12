from rest_framework import generics
from rest_framework import permissions

from .models import Products
from .serializers import ProductsSerializer

class ProductsListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
