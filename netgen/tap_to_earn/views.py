from django.shortcuts import render, redirect
from .models import Games, GameImage
from .forms import GamesForm
from django.contrib import messages
import os
from django.contrib import messages
from .usecases import add_to_favorites_fn, remove_from_favorites_fn

def add_to_favorites(request, product_id: int):
    if add_to_favorites_fn(request, product_id):
        messages.success(request, "Successfully added to favorites")
    else:
        messages.warning(request, "You already have this product in your favorites")

    referee = request.META.get('HTTP_REFERER')
    return redirect(referee)

def remove_from_favorites(request, product_id: int):
    if remove_from_favorites_fn(request, product_id):
        messages.success(request, "Successfully removed from favorites")
    else:
        messages.error(request, "You don't have this product in your favorites")

    referee = request.META.get('HTTP_REFERER')
    return redirect(referee)
def tap_to_earn(request):
    games = Games.objects.all()
    images = GameImage.objects.all()
    context = {"games": []}
    for game in games:
        game_images = images.filter(game=game)
        context['games'].append({'game':game, 'images':game_images})
    context["favorites"] = request.session.get("favorites", [])
    return render(request, 'tap-to-earn.html', context)


def add_game(request):
    form = GamesForm()
    if request.method == 'POST':
        form = GamesForm(request.POST, request.FILES)
        form.instance.author_of_post = request.user
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