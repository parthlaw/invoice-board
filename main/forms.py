from django import forms
from .models import Shop, item, sales, stock
import logging
logger = logging.getLogger('log')


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'


class StockForm(forms.ModelForm):
    shop = forms.ModelChoiceField(Shop.objects)
    item = forms.ModelChoiceField(item.objects)

    class Meta:
        model = stock
        fields = ['shop', 'item', 'quantity', 'MRP',
                  'cost_price', 'mfg_date', 'expiry']


class ItemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = '__all__'


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = sales
        fields = '__all__'
