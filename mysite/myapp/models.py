from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse('myapp:products')


    seller=models.ForeignKey(to=User,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    desc=models.CharField(max_length=250)
    image=models.ImageField(blank=True,upload_to='images')
    
## for payment gateway

class OrderDetail(models.Model):
    customer_username=models.CharField(max_length=100)
    product = models.ForeignKey(to=Product,on_delete=models.PROTECT)
    price = models.IntegerField()
    stripe_payment_intent = models.CharField(max_length=200)
    has_paid=models.BooleanField(default=False)
    createdon=models.DateTimeField(auto_now_add=True)
    updatedon=models.DateTimeField(auto_now_add=True)