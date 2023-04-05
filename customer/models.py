from django.db import models
from common.models import Customer
from  adbook.models import Productsss
from datetime import date


# Create your models here.



class Carts(models.Model):
    Customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    Product = models.ForeignKey(Productsss, on_delete= models.CASCADE)
    quantity =models.BigIntegerField()


class Wishlist(models.Model):
    Customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    Product = models.ForeignKey(Productsss, on_delete= models.CASCADE)


class Orders(models.Model):
    customer =models.ForeignKey(Customer,on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    status = models.CharField(max_length=20,default="pending")
    provider_order_id = models.CharField( max_length=40,default='' )
    payment_id = models.CharField(max_length=36,default='')
    signature_id = models.CharField(max_length=128,default='' )


    class Meta :
        db_table = 'order'

    def __str__(self):
        return f"{self.id}-{self.name}-{self.status}"



class Order_detail(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    productid = models.ForeignKey(Productsss,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.IntegerField()
    date = models.DateField(default=date.today)
    status = models.CharField(max_length=20,default="pending") #update after payment confirmed
    payment_type = models.CharField(max_length=20,default='')
    order=models.ForeignKey(Orders,on_delete=models.CASCADE,default=0)

    class Meta :
        db_table = 'order_dt'