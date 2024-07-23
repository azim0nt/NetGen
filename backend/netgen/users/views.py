from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile
from tap_to_earn.models import Games
from django.contrib.auth.models import User


@login_required
def profile_page(request, username=None):

    user = get_object_or_404(User, username=username)

    obj = get_object_or_404(Profile, user=user)
    games = Games.objects.filter(author_of_post=user)

    context = {
        "obj": obj,
        "games": games
    }
    return render(request, "profile_page.html", context)