from django.urls import path
from . import views

urlpatterns = [
    path('single-product/<slug:slug>', views.productView)
]
