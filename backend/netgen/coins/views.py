from django.shortcuts import render
from django.contrib.auth.decorators import login_required
@login_required
def coins(request):
    return render(request, 'coins.html')
