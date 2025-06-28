from django.urls import path
from . import views

urlpatterns = [
    path('products/<slug:slug>', views.ProductList.as_view(), name='product-list'),
    path('product/<slug:slug>', views.ProductDetail.as_view(), name='product-detail'),
]
