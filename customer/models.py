from django.db import models
from common.models import Customer
from  adbook.models import Productsss


# Create your models here.



class Carts(models.Model):
    Customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    Product = models.ForeignKey(Productsss, on_delete= models.CASCADE)


class Wishlist(models.Model):
    Customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    Product = models.ForeignKey(Productsss, on_delete= models.CASCADE)


