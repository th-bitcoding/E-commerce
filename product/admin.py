from django.contrib import admin
from product.models import Products
# Register your models here.
@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display =['id','owner','category','product_name','quantity','price']
