
from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_id = models.AutoField(auto_created=True,primary_key=True)
    customer_firstName = models.CharField(max_length=25)
    customer_lastName = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    customer_password = models.CharField(max_length=25)
    
    class Meta:
        db_table = "butta_customer"