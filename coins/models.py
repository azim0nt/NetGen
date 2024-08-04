# coins/models.py

from django.db import models

class Coin(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    market_cap = models.DecimalField(max_digits=20, decimal_places=2)
    total_supply = models.DecimalField(max_digits=20, decimal_places=2)
    current_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.total_supply > 0:
            self.current_price = self.market_cap / self.total_supply
        else:
            self.current_price = 0

        super().save(*args, **kwargs)

    def update_market_cap(self, amount, is_buying):
        if is_buying:
            self.market_cap += amount
        else:
            self.market_cap -= amount
        self.save()

    def update_total_supply(self, amount, is_buying):
        if is_buying:
            self.total_supply -= amount
        else:
            self.total_supply += amount
        self.save()

    def __str__(self):
        return f'#{self.id} {self.name} price: {self.current_price}'
