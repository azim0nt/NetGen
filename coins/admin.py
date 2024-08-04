from django.contrib import admin
from .models import Coin

class CoinAdmin(admin.ModelAdmin):
    # Определите список полей, которые должны отображаться в админке
    fields = ['name', 'symbol', 'market_cap', 'total_supply']  # Убедитесь, что current_price не включен


    # Не включайте current_price в список редактируемых полей
    readonly_fields = ['current_price']  # Делает поле только для чтения, если нужно показывать

admin.site.register(Coin, CoinAdmin)
