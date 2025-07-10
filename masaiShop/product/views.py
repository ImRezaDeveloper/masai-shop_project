from django.shortcuts import render
from .models import ProductModel, ProductBrand, Category, Comment, AdditionalFeature
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, View
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .mixin import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.urls import reverse

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

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brands = ProductBrand.objects.filter(product_brand__category__slug=self.kwargs['category_slug'])
        features = AdditionalFeature.objects.filter(product__category__slug=self.kwargs['category_slug'])
        context['brands'] = brands
        context['features'] = features
        return context
    
class ProductDetail(DetailView):
    template_name = 'product/single-product.html'
    model = ProductModel
    context_object_name = 'product'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if 'slug' in self.kwargs:
            queryset = queryset.filter(slug=self.kwargs['slug'])
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        connected_likes = get_object_or_404(ProductModel, slug=self.kwargs['slug'])
        liked = False
        
        if connected_likes.likes.filter(id=self.request.user.id).exists():
            liked = True
            
        context['number_of_likes'] = connected_likes.number_of_likes()
        context['product_is_liked'] = liked
        # context["product"] = get_object_or_404(ProductModel)
        context["comments"] = Comment.objects.all()
        context['features'] = AdditionalFeature.objects.all()

        return context
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()  # ← نمونه‌ی فرم
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = self.object
            comment.user = request.user
            comment.save()
            return redirect(self.request.path)
        else:
            context = self.get_context_data()
            context['form'] = form
            return render(request, 'product/single-product.html', context)
        
        
def prodcut_like(request, slug):
    product = get_object_or_404(ProductModel, slug=slug)
    
    if product.likes.filter(id=request.user.id).exists():
        product.likes.remove(request.user)
    else:
        product.likes.add(request.user)
    
    return HttpResponseRedirect(reverse('product-detail', args=[slug]))