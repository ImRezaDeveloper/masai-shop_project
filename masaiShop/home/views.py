from django.shortcuts import render
from django.views.generic import View
from product.models import Category, ProductModel
# Create your views here.

class HomeView(View):
    def get(self, request):
        categories = Category.objects.all()
        products = ProductModel.objects.all()
        products_isOffer = ProductModel.objects.filter(is_offer=True)
        return render(request, 'base.html', {'categories': categories, 'products': products, 'products_isOffer': products_isOffer})