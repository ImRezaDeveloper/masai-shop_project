from .models import Category, ProductBrand

def show_categories(request):
    return {'categories': Category.objects.all()}

def show_brands(request):
    return {'brands': ProductBrand.objects.all()}