from django.urls import path
from .views import *

urlpatterns = [
   path('', coins, name='coins'),
]