from django.shortcuts import render
from .models import ProductModel
from django.shortcuts import get_object_or_404

# Create your views here.

def productView(request, slug):
    product = get_object_or_404(ProductModel, slug=slug)
    return render(request, 'product/single-product.html', context={'product': product})
