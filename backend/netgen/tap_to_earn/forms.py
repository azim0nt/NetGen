from django.forms import forms, ModelForm
from .models import Games

class GamesForm(ModelForm):
    class Meta:
        model = Games
        fields = [ 'name', 'platform', 'about', 'link']