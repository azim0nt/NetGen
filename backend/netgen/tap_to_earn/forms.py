from django import forms
from .models import Games

class GamesForm(forms.ModelForm):
    image = forms.ImageField(label='Image', required=False, widget=forms.FileInput(attrs={'class':'form-control'}))
    class Meta:
        model = Games
        fields = [ 'name', 'platform', 'about', 'link', 'image']