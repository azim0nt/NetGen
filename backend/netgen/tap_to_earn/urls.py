from django.urls import path
from .views import *

urlpatterns = [
    path('', tap_to_earn, name='tap_to_earn')
]