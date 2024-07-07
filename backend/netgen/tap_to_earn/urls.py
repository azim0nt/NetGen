from django.urls import path
from .views import *

urlpatterns = [
    path('', tap_to_earn, name='tap-to-earn'),
    path('add-game/',add_game, name='add-game'),
    path('update-game/game-<int:pk>',update_game, name='update-game')
]