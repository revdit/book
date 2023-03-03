from django.db import models

# Create your models here.
# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    phone_number = models.BigIntegerField()
    gender = models.CharField(max_length=50)
    email_address = models.CharField(max_length=30)
    cust_password = models.CharField(max_length=10)

class Seller(models.Model):
        username= models.CharField(max_length=50)
        password = models.CharField(max_length=50)
 
    