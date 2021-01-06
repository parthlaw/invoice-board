from django import forms 

from .models import Shop
from .models import stock


class ShopForm(forms.ModelForm):
    class Meta:
        model=Shop
        fields= '__all__'
<<<<<<< HEAD
=======

class StockForm(forms.ModelForm):
    class Meta:
        model=stock
        fields= '__all__'

>>>>>>> b95e064e0994458bab61c7a33a438ebfb3321509
