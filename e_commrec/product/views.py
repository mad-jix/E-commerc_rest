from rest_framework import generics
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination

from .models import Products
from .serializers import ProductsSerializer

class ProductPage(PageNumberPagination):
    page_size = 1
    page_query_param = 'page_no'

class ProductsListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Products.objects.all()
    pagination_class = ProductPage
    serializer_class = ProductsSerializer


class ProductsDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = 'id'
