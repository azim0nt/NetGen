from rest_framework import generics
from .models import *
from .serializers import *

class GamesListCreate(generics.ListCreateAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    
    
class SingleGameView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer