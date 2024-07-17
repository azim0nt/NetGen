from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User

def users(request):
    context = {
        "title": "Hello world from Views",
        "content": "This is the content of the page"
    }
    return render(request, "users.html", context)


@login_required
def profile_page(request, username=None):
    user = get_object_or_404(User, username=username)
    try:
        obj = user.profile
    except Profile.DoesNotExist:
        obj = Profile.objects.create(user=user)
    return render(request, "profile_page.html", {"obj": obj})