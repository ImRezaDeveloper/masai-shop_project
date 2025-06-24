from django.utils.text import slugify
from django.db import models

class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    info = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products', null=True, blank=True)
    color = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    slug = models.SlugField(null=True, blank=True, unique=True, max_length=100)  # اضافه کردن unique=True
    discount = models.IntegerField(default=0)
    bluetooth = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

            
class AdditionalFeature(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="features")  # اضافه کردن related_name برای دسترسی آسانتر
    resolution_pic = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    waterproof = models.BooleanField(default=False)  # حذف null=True چون BooleanField نیازی به آن ندارد
    os = models.CharField(max_length=50, null=True, blank=True)
    technology = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Features of {self.product.title}"