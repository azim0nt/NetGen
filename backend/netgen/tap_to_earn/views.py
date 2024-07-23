from django.shortcuts import render, redirect
from .models import Games, GameImage
from .forms import GamesForm
from django.contrib import messages
import os
from django.contrib import messages
def tap_to_earn(request):
    games = Games.objects.all()
    images = GameImage.objects.all()
    context = {"games": []}
    for game in games:
        game_images = images.filter(game=game)
        context['games'].append({'game':game, 'images':game_images})
    return render(request, 'tap-to-earn.html', context)


def add_game(request):
    form = GamesForm()
    if request.method == 'POST':
        form = GamesForm(request.POST, request.FILES)
        images = request.FILES.getlist('images')
        if form.is_valid():
            form.save()
            for img in images:
                GameImage.objects.create(game=form.instance, image=img)
            messages.success(request, 'Game added successfully')
            return redirect('tap-to-earn')
    context = {'form': form, 'multiple_image':True}
    return render(request, 'add_game.html', context)


def update_game(request, pk: int):
    game = Games.objects.get(id=pk)
    form = GamesForm(instance=game)
    if request.method == 'POST':
    
        form = GamesForm(request.POST, request.FILES, instance=game)
        
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


def game_details(request, pk:int):
    game = Games.objects.get(id=pk)
    context = {'game':game, 'images':GameImage.objects.filter(game=pk)}
    return render(request, 'game_details.html', context)