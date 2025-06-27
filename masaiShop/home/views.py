from django.shortcuts import render
from django.views.generic import View
from product.models import Category
# Create your views here.

class HomeView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'base.html', {'categories': categories})