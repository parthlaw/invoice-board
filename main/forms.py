from django import  forms
from .models import Shop
from .models import stock


class ShopForm(forms.ModelForm):
    class Meta:
        model=Shop
        fields= '__all__'

class StockForm(forms.ModelForm):
    class Meta:
        model=stock
        fields= '__all__'

