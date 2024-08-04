# market/models.py

from django.db import models
from django.conf import settings
from coins.models import Coin

class UserCoin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.username} - {self.coin.name}: {self.amount}"

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE) 
    transaction_type = models.CharField(max_length=4, choices=TRANSACTION_TYPES) 
    amount = models.DecimalField(max_digits=20, decimal_places=2)  
    price_per_coin = models.DecimalField(max_digits=20, decimal_places=2)  
    total_price = models.DecimalField(max_digits=20, decimal_places=2)  
    timestamp = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.transaction_type.capitalize()} {self.amount} {self.coin.name} by {self.user.username}"
