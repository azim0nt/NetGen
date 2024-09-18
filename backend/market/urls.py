from django.urls import path
from . import views



urlpatterns = [
    path('buy/<int:coin_id>/', views.buy_coin, name='buy_coin'),
    path('sell/<int:coin_id>/', views.sell_coin, name='sell_coin'),
]
