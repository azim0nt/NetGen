from django.shortcuts import render, redirect
from .models import Games
from .forms import GamesForm
from django.contrib import messages
import os

def tap_to_earn(request):
    context = {
        "games": Games.objects.all()
    }
    return render(request, 'tap-to-earn.html', context)


def add_game(request):
    form = GamesForm()
    if request.method == 'POST':
        form = GamesForm(request.POST, request.FILES)
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
        
        old_image = Games.objects.get(id=pk)
        form = GamesForm(request.POST, request.FILES, instance=old_image)
        
        if form.is_valid():
            game.name = form.cleaned_data.get('name')
            game.platform = form.cleaned_data.get('platform')
            game.about = form.cleaned_data.get('about')
            game.link = form.cleaned_data.get('link')
            game.image = form.cleaned_data.get('image')
            image_path = old_image.image.path
            if os.path.exists(image_path):
                os.remove(image_path)
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


def game_details(request, pk:int):
    game = Games.objects.get(id=pk)
    context = {'game':game}
    return render(request, 'game_details.html', context)