from django.db import models
from base.models import MyModel
from Client.models import Category,Client
# Create your models here.
class Products(MyModel):
    owner = models.ForeignKey(Client,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.product_name