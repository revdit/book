from django.db import models
from common.models import Seller
from common.models import Customer




# Create your models here.



class Author(models.Model):

    author_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='author/',default='')




class Products(models.Model):
    seller = models.ForeignKey(Seller,on_delete= models.CASCADE)
    author = models.ForeignKey(Author,on_delete= models.CASCADE,default='')
   
    
    product_name = models.CharField(max_length=30)
    product_description = models.CharField(max_length=100)
    product_number = models.BigIntegerField()
  
    language =models.CharField(max_length=50,default='')
    stock = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to='product/',default='')    









class Order(models.Model):
    Customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    Product = models.ForeignKey(Products, on_delete= models.CASCADE)
