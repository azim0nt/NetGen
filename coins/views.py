# coins/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.utils.dateformat import format
from django.core.serializers.json import DjangoJSONEncoder
from .models import Coin, CoinPriceHistory
import json
from .forms import CoinsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _


def coin_list(request):
    coins = Coin.objects.all()
    context = {
        'coins': coins,
        "coins_list": _("Список криптовалют"),
        "add_coin": _("Добавить монету"),
        "currency": _("Валюта"),
        "price": _("Цена"),
        "capitalization": _("Капитализация"),
        "number_of_coins": _("Количество монет")


    }
    return render(request, 'coins.html', context)


def coin_detail(request, pk):
    coin = get_object_or_404(Coin, pk=pk)
    price_history = CoinPriceHistory.objects.filter(
        coin=coin).order_by('timestamp')
    prices = [(int(history.timestamp.timestamp() * 1000),
               float(history.price)) for history in price_history]

    # Convert to JSON with proper formatting
    prices_json = json.dumps(prices, cls=DjangoJSONEncoder)

    return render(request, 'coin_detail.html', {'coin': coin, 'prices': prices_json})


@login_required
def add_coin(request):
    if request.method == 'POST':
        form = CoinsForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save(commit=False)
            game.author_of_post = request.user
            game.save()
            messages.success(request, 'Coin added successfully')
            return redirect('tap-to-earn')
        else:
            messages.error(
                request, 'There was an error with your form. Please correct the errors and try again.')
    else:
        form = CoinsForm()

    context = {'form': form}
    return render(request, 'add_coin.html', context)


@login_required
def update_coin(request, pk: int):
    coin = Coin.objects.get(id=pk)
    form = CoinsForm(instance=coin)
    if request.method == 'POST':

        form = CoinsForm(request.POST, request.FILES, instance=coin)

        if form.is_valid():
            coin.name = form.cleaned_data.get('name')
            coin.symbol = form.cleaned_data.get('symbol')
            coin.market_cap = form.cleaned_data.get('market_cap')
            coin.total_supply = form.cleaned_data.get('total_supply')

            coin.save()
            messages.success(request, 'Coin updated successfully')
            return redirect('tap-to-earn')
    context = {
        'form': form,
        'coin': coin
    }
    return render(request, 'update_coin.html', context)
