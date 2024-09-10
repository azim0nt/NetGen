from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


def home(request):
    context = {
        "home":_("Главная"),
        "we_doing_crypto":_("Мы делаем крипту"),
        "understandable":_("понятной"),
        "and_simple":_("и простой"),
        "subtitle":_("Создавайте, покупайте и развивайте свою криптовалюту с помощью CoinFlip, платформы, предназначенной для каждого трейдера на любом уровне."),
        "get_started":_("Начать")
        
    }
    return render(request, "home.html", context)