from django.db import models
from base.models import MyModel
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Client(AbstractUser,MyModel):

    gender_choice =(
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other')
    )
    
    email = models.EmailField(unique=True)
    gender = models.CharField(choices=gender_choice,default='Male',max_length=6)
    address = models.TextField()
    DOB = models.DateField(auto_now=False,null=True)
    phone_number = models.CharField(max_length=13)
    image = models.ImageField(upload_to ='profile/')


    def __str__(self):
        return self.username
    
class Category(MyModel):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category
    

# class Product(MyModel):
#     owner = models.ForeignKey(Client,on_delete=models.CASCADE)
#     product_name = models.CharField(max_length=100)
#     product_image = models.ImageField(upload_to ='products/')
#     description = models.TextField()
