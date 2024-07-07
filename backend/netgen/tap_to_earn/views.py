from django.shortcuts import render, redirect
from .models import Games
from .forms import GamesForm
from django.contrib import messages
def tap_to_earn(request):
    context = {
        "games":Games.objects.all()
    }
    return render(request, 'tap-to-earn.html', context)

def add_game(request):
    form = GamesForm()
    if request.method == 'POST':
        form = GamesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Game added successfully')
            return redirect('tap-to-earn')
    context = {'form':form}
    return render(request, 'add_game.html', context) 