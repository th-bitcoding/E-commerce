from django.contrib import admin
from Client.models import Client,Category
# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display =['id','username','email']

@admin.register(Category)
class ClientAdmin(admin.ModelAdmin):
    list_display =['id','category']