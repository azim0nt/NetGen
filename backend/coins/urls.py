from django.urls import path
from .views import *

urlpatterns = [
   path('', coin_list, name='coin_list'),
   path('<int:pk>/', coin_detail, name='coin_detail'),
   path('add_coin', add_coin, name='add_coin'),
   path('update_coin/<int:pk>',update_coin, name='update_coin')
]