from django.shortcuts import render
from .models import ProductModel, ProductBrand, Category, Comment, AdditionalFeature, Color
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
        queryset = ProductModel.objects.all()
        request = self.request

        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        colors = request.GET.getlist('colors')
        brands = request.GET.getlist('brand')
        os_list = request.GET.getlist('os')

        if colors:
            queryset = queryset.filter(color__name__in=colors)

        if brands:
            queryset = queryset.filter(brand__slug__in=brands)

        if os_list:
            queryset = queryset.filter(features__os__in=os_list)

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category_slug = self.kwargs.get('category_slug')
        selected_brand = self.request.GET.get('brand')

        if category_slug:
            context['brands'] = ProductBrand.objects.filter(product_brand__category__slug=category_slug).distinct()
            context['features'] = AdditionalFeature.objects.filter(product__category__slug=category_slug).distinct()
        else:
            context['brands'] = ProductBrand.objects.all()
            context['features'] = AdditionalFeature.objects.all()

        if selected_brand:
            context['colors'] = Color.objects.filter(product_color__brand__slug=selected_brand).distinct()
        elif category_slug:
            context['colors'] = Color.objects.filter(product_color__category__slug=category_slug).distinct()
        else:
            context['colors'] = Color.objects.all()


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
        context['colors'] = Color.objects.filter(product_color__name=self.kwargs['slug'])

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
