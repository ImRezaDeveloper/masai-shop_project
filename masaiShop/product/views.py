from django.shortcuts import render
from .models import ProductModel, Category, Comment
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
# Create your views here.

# def productView(request, slug):
#     product = get_object_or_404(ProductModel, slug=slug)
#     return render(request, 'product/single-product.html', context={'product': product})

class ProductList(ListView):
    template_name = 'product/products.html'
    model = ProductModel
    context_object_name = 'products'      
        
    def get_queryset(self):
        queryset = super().get_queryset()
        if 'category_slug' in self.kwargs:
            queryset = queryset.filter(category__slug=self.kwargs['category_slug'])

        brandSlug = self.request.GET.get('brand')
        if brandSlug:
            queryset = queryset.filter(brand__slug=brandSlug)
            
        return queryset
    
class ProductDetail(DetailView):
    template_name = 'product/single-product.html'
    model = ProductModel, Comment
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