from django.db import models

# Create your models here.

class Product(models.Model):
    
    name = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.CharField(max_length=80)
    category = models.CharField(max_length=30)
    gender = models.CharField(max_length=6)
    size = models.CharField(max_length=3)
    color = models.CharField(max_length=10)
    brand = models.CharField(max_length=20)
    purchase_date = models.CharField(max_length=15)
    packaged = models.CharField(max_length=15)
    user = models.CharField(max_length=20)
    post_date = models.CharField(max_length=15)
    image_name = models.CharField(max_length=200)
    order_id = models.IntegerField()
