
from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction
from coins.models import Coin
from django.http import HttpResponse
from django.db import transaction as db_transaction
from django.contrib.auth.decorators import login_required
from decimal import Decimal
# market/views.py

from .models import Transaction, UserCoin

@login_required
def buy_coin(request, coin_id):
    coin = get_object_or_404(Coin, id=coin_id)
    if request.method == 'POST':
        amount = Decimal(request.POST.get('amount'))
        total_price = coin.current_price * amount
        user = request.user

        if user.usdt_balance < total_price:
            return HttpResponse("Недостаточно средств", status=400)

        with db_transaction.atomic():
            # Обновляем или создаем запись UserCoin
            user_coin, created = UserCoin.objects.get_or_create(user=user, coin=coin)
            user_coin.amount += amount
            user_coin.save()

            # Создаем транзакцию
            Transaction.objects.create(
                user=user,
                coin=coin,
                transaction_type='buy',
                amount=amount,
                price_per_coin=coin.current_price,
                total_price=total_price
            )

            # Обновляем баланс пользователя
            user.usdt_balance -= total_price
            user.save()

        return redirect('coin_list')
    return render(request, 'buy_coin.html', {'coin': coin})

@login_required
def sell_coin(request, coin_id):
    coin = get_object_or_404(Coin, id=coin_id)
    if request.method == 'POST':
        amount = Decimal(request.POST.get('amount'))
        total_price = coin.current_price * amount
        user = request.user

        # Проверяем, есть ли у пользователя достаточно монет для продажи
        user_coin = UserCoin.objects.filter(user=user, coin=coin).first()
        if not user_coin or user_coin.amount < amount:
            return HttpResponse("Недостаточно монет для продажи", status=400)

        with db_transaction.atomic():
            # Обновляем количество монет у пользователя
            user_coin.amount -= amount
            user_coin.save()

            # Создаем транзакцию
            Transaction.objects.create(
                user=user,
                coin=coin,
                transaction_type='sell',
                amount=amount,
                price_per_coin=coin.current_price,
                total_price=total_price
            )

            # Обновляем баланс пользователя
            user.usdt_balance += total_price
            user.save()

        return redirect('coin_list')
    return render(request, 'sell_coin.html', {'coin': coin})
