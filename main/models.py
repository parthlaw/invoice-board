from django.db import models

# Create your models here.
class Shop(models.Model):
    shop_name = models.CharField(max_length=42)
    created_on = models.DateTimeField(auto_now_add=True)
    address=models.TextField()

    class Meta:
        db_table="Shop"

class item(models.Model):
    item_name = models.CharField(max_length=42)
    cost_price= models.FloatField()
    company=models.TextField()
    item_type=models.TextField()
 
    class Meta:
        db_table="item"

class stock(models.Model):
    shop_id = models.ForeignKey(Shop,on_delete=models.CASCADE)
    item_id =  models.ForeignKey(item,on_delete=models.CASCADE)
    Date= models.DateTimeField(auto_now_add=True)
    quantity=models.IntegerField()
    MRP = models.FloatField()
    mfg_date= models.DateTimeField(auto_now_add=True)
    expiry= models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table="stock"

class sales(models.Model):
    invoice_no = models.IntegerField()
    item_id =  models.ForeignKey(item,on_delete=models.CASCADE)
    shop_id =  models.ForeignKey(Shop,on_delete=models.CASCADE)
    quantity=  models.IntegerField()
    cus_name=   models.CharField(max_length=42)
    sell_price= models.FloatField()

    class Meta:
        db_table="sales"


class inventory(models.Model):
    item_id =  models.ForeignKey(item,on_delete=models.CASCADE)
    shop_id =  models.ForeignKey(Shop,on_delete=models.CASCADE)
    quantity= models.IntegerField()

    class Meta:
        db_table="inventory"

    