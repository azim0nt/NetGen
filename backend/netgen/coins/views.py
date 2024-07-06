from django.shortcuts import render

def coins(request):
    return render(request, 'coins.html')
