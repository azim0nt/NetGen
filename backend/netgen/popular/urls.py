from django.urls import path
from .views import *

urlpatterns = [
   path('', popular, name='popular'),
]