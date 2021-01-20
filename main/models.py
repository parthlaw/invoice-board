from django.db import models
from django.contrib.auth.models import User
import datetime


class Shop(models.Model):
    shop_name = models.CharField(max_length=42)
    created_on = models.DateTimeField(auto_now_add=True)
    address = models.TextField()

    def __str__(self):
        return self.shop_name


class item(models.Model):
    item_name = models.CharField(max_length=42)
    company = models.TextField()
    item_type = models.TextField()

    def __str__(self):
        return self.item_name


class stock(models.Model):
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    item_id = models.ForeignKey(item, on_delete=models.CASCADE)
    Date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    MRP = models.FloatField()
    cost_price = models.FloatField()
    mfg_date = models.DateField()
    expiry = models.DateField()


class sales(models.Model):
    invoice_id = models.CharField(max_length=42)
    stock_id = models.ForeignKey(stock, on_delete=models.CASCADE)
    item_id = models.ForeignKey(item, on_delete=models.CASCADE)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    cus_name = models.CharField(max_length=42)
    sell_price = models.FloatField()

    def save(self, *args, **kwargs):
        today = datetime.date.today()
        today_string = today.strftime('%y%m%d')
        next_invoice_number = '01'
        last_invoice = Invoice.objects.filter(
            invoice_id__startswith=today_string).order_by('invoice_id').last()
        if last_invoice:
            last_invoice_number = int(last_invoice.invoice_id[6:])
            next_invoice_number = '{0:02d}'.format(last_invoice_number + 1)
        self.invoice_id = today_string + next_invoice_number
        super(Invoice, self).save(*args, **kwargs)


class inventory(models.Model):
    item_id = models.ForeignKey(item, on_delete=models.CASCADE)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'
