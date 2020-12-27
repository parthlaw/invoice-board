from django.db import models

# Create your models here.

class Shop(models.Model):
    shop_name = models.CharField(max_length=42)
    created_on = models.DateTimeField(auto_now_add=True)
    address=models.TextField()
    