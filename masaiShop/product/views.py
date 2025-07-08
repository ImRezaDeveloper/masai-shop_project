from django.shortcuts import render
from .models import ProductModel, Category, Comment, AdditionalFeature, Like
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, View
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .mixin import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.http import JsonResponse
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
    model = ProductModel
    context_object_name = 'product'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if 'slug' in self.kwargs:
            queryset = queryset.filter(slug=self.kwargs['slug'])
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        user = self.request.user
        # context["product"] = get_object_or_404(ProductModel)
        context["comments"] = Comment.objects.all()
        context['features'] = AdditionalFeature.objects.all()

        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # همون محصول جاری
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = self.object
            comment.user = request.user
            comment.save()
            return redirect(self.request.path)  # بهتر از render برای جلوگیری از ارسال مجدد
        else:
            context = self.get_context_data(form=form)
            return self.render_to_response(context)

# @method_decorator(login_required, name='dispatch')
# class LikeProductView(View):
#     def get(self, request, slug):
#         product = get_object_or_404(ProductModel, slug=slug)
#         liked = Like.objects.filter(user=request.user, product=product).exists()
#         like_count = product.product_like.count()
#         return JsonResponse({'liked': liked, 'like_count': like_count})

#     def post(self, request, slug):
#         product = get_object_or_404(ProductModel, slug=slug)
#         like, created = Like.objects.get_or_create(user=request.user, product=product)
#         if not created:
#             like.delete()
#             liked = False
#         else:
#             liked = True
#         like_count = product.product_like.count()
#         return JsonResponse({'liked': liked, 'like_count': like_count})
