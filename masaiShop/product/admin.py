from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.ProductModel)
class ProdcutAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    
@admin.register(models.ProductBrand)
class ProdcutBrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    


admin.site.register(models.AdditionalFeature)
admin.site.register(models.Like)
admin.site.register(models.Comment)