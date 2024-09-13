from django.urls import path
from tap_to_earn.api_views import GamesListCreate, SingleGameView
urlpatterns = [
    path('game-list/',GamesListCreate.as_view()),
    path('game/<int:pk>/', SingleGameView.as_view())
]