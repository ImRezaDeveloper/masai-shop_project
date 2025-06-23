from django.db import models

# Create your models here.

class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    info = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products')
    color = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    bluetooth = models.BooleanField(default=True)

    def __str__(self):
        return self.title
        
class AdditionalFeature(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    resolution_pic = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    waterproof = models.BooleanField(default=False, null=True, blank=True)
    os = models.CharField(max_length=50, null=True, blank=True)
    technology = models.CharField(max_length=100, null=True, blank=True)