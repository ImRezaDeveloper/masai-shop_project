from django.shortcuts import render
from .models import ProductModel, Category
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
# Create your views here.

# products
class ProductList(De):
    template_name = 'product/products.html'
    model = ProductModel

    context_object_name = 'products'
class ProductDetail(DetailView):
    template_name = 'product/single-product.html'
    model = ProductModel
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] = get_object_or_404(ProductModel)
        return context
    
# categories 