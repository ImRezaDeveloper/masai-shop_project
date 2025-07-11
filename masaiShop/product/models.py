from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subs', null=True, blank=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories', null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True, max_length=100)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
class ProductBrand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
class Color(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    info = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products', null=True, blank=True)
    color = models.ManyToManyField(Color, related_name='product_color')
    price = models.IntegerField(default=0)
    slug = models.SlugField(null=True, blank=True, unique=True, max_length=100)  # اضافه کردن unique=True
    discount = models.IntegerField(default=0)
    bluetooth = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category', null=True, blank=True)
    is_offer = models.BooleanField(default=True)
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, related_name='product_brand', null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='product_like')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def number_of_likes(self):
        return self.likes.count()
            
class AdditionalFeature(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="features")  # اضافه کردن related_name برای دسترسی آسانتر
    resolution_pic = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    waterproof = models.BooleanField(default=False)  # حذف null=True چون BooleanField نیازی به آن ندارد
    os = models.CharField(max_length=50, null=True, blank=True)
    technology = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Features of {self.product.title}"
    
class Comment(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=500)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    # image = models.ImageField(upload_to='users', null=True, blank=True)
    
    def __str__(self):
        return self.title
