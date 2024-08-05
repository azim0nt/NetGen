# coins/views.py

from django.shortcuts import render, get_object_or_404
from django.utils.dateformat import format
from django.core.serializers.json import DjangoJSONEncoder
from .models import Coin, CoinPriceHistory
import json

def coin_list(request):
    coins = Coin.objects.all()
    return render(request, 'coins.html', {'coins': coins})

def coin_detail(request, pk):
    coin = get_object_or_404(Coin, pk=pk)
    price_history = CoinPriceHistory.objects.filter(coin=coin).order_by('timestamp')
    prices = [(int(history.timestamp.timestamp() * 1000), float(history.price)) for history in price_history]
    
    # Convert to JSON with proper formatting
    prices_json = json.dumps(prices, cls=DjangoJSONEncoder)
    
    return render(request, 'coin_detail.html', {'coin': coin, 'prices': prices_json})
