from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Coin


def coin_list(request):
    coins = Coin.objects.all()  # Получаем все криптовалюты
    return render(request, 'coins.html', {'coins': coins})

def coin_detail(request, pk):
    coin = get_object_or_404(Coin, pk=pk)  # Получаем криптовалюту по первичному ключу
    return render(request, 'coin_detail.html', {'coin': coin})
