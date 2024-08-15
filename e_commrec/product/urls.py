from django.urls import path, include


from .views import ProductsListView,ProductsDetailView


urlpatterns = [
    path('products/',ProductsListView.as_view(),name = "products"),
    path('detailview/<int:id>/',ProductsDetailView.as_view(),name = "product-detail"),
]
