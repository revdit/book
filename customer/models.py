from django.db import models
from common.models import Customer
from  adbook.models import Products


# Create your models here.



class Carts(models.Model):
    Customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    Product = models.ForeignKey(Products, on_delete= models.CASCADE)


class Wishlist(models.Model):
    Customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    Product = models.ForeignKey(Products, on_delete= models.CASCADE)


