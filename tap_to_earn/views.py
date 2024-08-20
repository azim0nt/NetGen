from django.shortcuts import render, redirect
from .models import Games
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
    context = {"games": []}
    for game in games:
        context['games'].append({'game':game})
    context["favorites"] = request.session.get("favorites", [])
    return render(request, 'tap-to-earn.html', context)


def add_game(request):
    if request.method == 'POST':
        form = GamesForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save(commit=False)
            game.author_of_post = request.user
            game.save()
            messages.success(request, 'Game added successfully')
            return redirect('tap-to-earn')
        else:
            messages.error(request, 'There was an error with your form. Please correct the errors and try again.')
    else:
        form = GamesForm()

    context = {'form': form}
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
    context = {'game':game}
    return render(request, 'game_details.html', context)