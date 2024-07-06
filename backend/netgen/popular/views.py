from django.shortcuts import render

def popular(request):
    return render(request, 'popular.html')
