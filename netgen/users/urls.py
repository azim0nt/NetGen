from django.urls import path
from .views import *

urlpatterns = [
    path("profile/<str:username>/", profile_page, name='profile_page'),
]
