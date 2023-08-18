from django import forms
from product.models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['owner','category','product_name','image','description','quantity','price']