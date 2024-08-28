from django import forms
from .models import Coin

class CoinsForm(forms.ModelForm):
    class Meta:
        model = Coin
        fields = ["name","symbol","market_cap","total_supply","image"]