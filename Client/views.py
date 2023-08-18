from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from Client.models import Client,Category
from Client.forms import ClientForm,CategoryForm
from string import digits
import random
from django.contrib.auth.mixins import LoginRequiredMixin
from base.mixins import SuperuserRequiredMixin
from django.views.generic import TemplateView,ListView

# Create your views here.

# def check(request,self):
#     if request.user.is_superuser():

def index(request):
    return render(request,'dashboard/index.html')

class CategoryCreate(CreateView):
    form_class = CategoryForm
    model = Category
    template_name = 'client/category.html'
    success_url = reverse_lazy('client:category')

class CategoryView(ListView):
    model = Category
    context_object_name='category'
    template_name = 'client/categorylist.html'


class ClientCreate(SuperuserRequiredMixin,CreateView):
    form_class = ClientForm
    model = Client
    template_name = 'client/user.html'
    success_url = reverse_lazy('client:add')
    

    def form_valid(self,form):
        email = form.cleaned_data['email']
        print('***',email)
        username = email.split('@')[0] + ''.join(random.choice(digits) for i in range(3))
        print('***',username)
        password = username + ''.join(random.choice(digits) for i in range(1))
        print('***',password)
        form.instance.username=username
        form.instance.set_password(password)
        form.save()
        return super().form_valid(form)