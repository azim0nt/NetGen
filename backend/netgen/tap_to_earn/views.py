from django.shortcuts import render, redirect
from .models import Games
from .forms import GamesForm
from django.contrib import messages


def tap_to_earn(request):
    context = {
        "games": Games.objects.all()
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
    context = {'form': form}
    return render(request, 'add_game.html', context)


def update_game(request, pk: int):
    game = Games.objects.get(id=pk)
    form = GamesForm(instance=game)
    if request.method == 'POST':
        form = GamesForm(request.POST)
        if form.is_valid():
            game.name = form.cleaned_data.get('name')
            game.platform = form.cleaned_data.get('platform')
            game.about = form.cleaned_data.get('about')
            game.link = form.cleaned_data.get('link')
            game.save()
            messages.success(request, 'Game updated successfully')
            return redirect('tap-to-earn')
    context = {
        'form': form,
        'game': game
    }
    return render(request, 'update_game.html', context)

def delete_game(request,pk:int):
    game = Games.objects.get(id=pk)
    game.delete()
    messages.success(request,"Game deleted successfully")
    return redirect('tap-to-earn')
