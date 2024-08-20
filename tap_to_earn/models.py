from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.conf import settings
import os



class Games(models.Model):
    PLATFORM_CHOICES = [
        ('Telegram', 'Telegram'),
        ('WebSite', 'WebSite'),
        ('Mobile app', 'Mobile app')
    ]
    name = models.CharField(max_length=50)
    platform = models.CharField(max_length=10, choices=PLATFORM_CHOICES)
    about = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    added_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='games/', default='games/default.png')
    author_of_post = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'

    def __str__(self):
        return self.name

