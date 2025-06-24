from django.shortcuts import render
from .models import ProductModel
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
# Create your views here.

# def productView(request, slug):
#     product = get_object_or_404(ProductModel, slug=slug)
#     return render(request, 'product/single-product.html', context={'product': product})


class ProductDetail(DetailView):
    template_name = 'product/single-product.html'
    model = ProductModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] = get_object_or_404(ProductModel)
        return context
    