from django.urls import path
from .views import *

urlpatterns = [
   path('', coin_list, name='coin_list'),
   path('<int:pk>/', coin_detail, name='coin_detail'),
]