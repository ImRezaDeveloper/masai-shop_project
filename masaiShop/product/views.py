from django.shortcuts import render
from .models import ProductModel, Category
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
# Create your views here.

# products
class ProductList(ListView):
    template_name = 'product/products.html'
    model = ProductModel
    context_object_name = 'products'  
        
    def get_queryset(self):
        queryset = super().get_queryset()
        if 'category_slug' in self.kwargs:
            queryset = queryset.filter(category__slug=self.kwargs['category_slug'])
        return queryset 
    
class ProductDetail(DetailView):
    template_name = 'product/single-product.html'
    model = ProductModel
    context_object_name = 'product'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if 'slug' in self.kwargs:
            queryset = queryset.filter(slug=self.kwargs['slug'])
        return queryset
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["product"] = get_object_or_404(ProductModel)
    #     return context