from django.urls import path

from .views import CartView

urlpatterns = [
    path('addtocart/',CartView.as_view(),name = "addtocart"),
]
