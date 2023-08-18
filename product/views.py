from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView
from Client.models import Category
from product.forms import ProductForm
from product.models import Products
from django.urls import reverse_lazy
# Create your views here.
class CategoryCreate(TemplateView):
    template_name = 'client/category.html'

class ProductCreate(CreateView):
    form_class = ProductForm
    model = Products
    template_name='product/addproduct.html'
    success_url = reverse_lazy('product:productadd')

class ProductList(ListView):
    model = Products
    context_object_name = 'product'
    template_name = 'product/productlist.html'

class ProductUpdate(UpdateView):
    form_class = ProductForm
    model = Products
    # fields = '__all__'
    template_name = 'product/addproduct.html'
    success_url = reverse_lazy('product:productlist')

class ProductDelete(DeleteView):
    model = Products
    template_name ='product/productdelete.html'
    success_url = reverse_lazy('product:productlist')

def index(request):
    return render(request,'customer/customer.html')

class CustomerProductList(ListView):
    model = Products
    context_object_name = 'product'
    template_name = 'customer/customer.html'
