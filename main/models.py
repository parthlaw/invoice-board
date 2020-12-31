from django.db import models
from django.contrib.auth.models import User





class Shop(models.Model):
    shop_name = models.CharField(max_length=42)
    created_on = models.DateTimeField(auto_now_add=True)
    address = models.TextField()


class item(models.Model):
    item_name = models.CharField(max_length=42)
    company = models.TextField()
    item_type = models.TextField()


class stock(models.Model):
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    item_id = models.ForeignKey(item, on_delete=models.CASCADE)
    Date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    MRP = models.FloatField()
    cost_price = models.FloatField()
    mfg_date = models.DateTimeField(auto_now_add=True)
    expiry = models.DateTimeField(auto_now_add=True)


class sales(models.Model):
    invoice_no = models.IntegerField()
    stock_id = models.ForeignKey(stock, on_delete=models.CASCADE)
    item_id = models.ForeignKey(item, on_delete=models.CASCADE)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    cus_name = models.CharField(max_length=42)
    sell_price = models.FloatField()


class inventory(models.Model):
    item_id = models.ForeignKey(item, on_delete=models.CASCADE)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    

   
    def __str__(self):
        return f'{self.user.username} Profile'
    