from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('products/<slug:category_slug>/', views.ProductList.as_view(), name='product-list-by-category'),
    path('product/<slug:slug>', views.ProductDetail.as_view(), name='product-detail'),
    path('product/like/<slug:slug>', views.LikeProductView.as_view(), name='product-like')
]
