from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from tap_to_earn.models import Games    
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.urls import reverse

@login_required
def profile_page(request, username=None):

    user = get_object_or_404(User, username=username)

    obj = get_object_or_404(Profile, user=user)
    favorites = [int(i) for i in request.session.get('favorites', []) ]
    
    
    games = Games.objects.filter(author_of_post=user)
    context = {
        "obj": obj,
        "games": games,
        "stars":Games.objects.filter(id__in=favorites)
    }
    return render(request, "profile_page.html", context)

def custom_logout(request):
    logout(request)
    return redirect(reverse('home'))