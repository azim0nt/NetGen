from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.conf import settings
import os
class GameImage(models.Model):
    game = models.ForeignKey('Games', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='games-icon/', default='games-icon/default.jpg')

    def __str__(self) -> str:
        return f'{self.id} image of {self.game.name}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image.name != 'games-icon/default.jpg':
            img = Image.open(self.image.path)
            webp_path = self.image.path.rsplit('.', 1)[0] + '.webp'
            img.save(webp_path, 'WEBP')

            if os.path.exists(self.image.path):
                os.remove(self.image.path)

            self.image.name = self.image.name.rsplit('.', 1)[0] + '.webp'

            super().save(update_fields=['image'])


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
    images = models.ManyToManyField(GameImage)
    author_of_post = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'

    def __str__(self):
        return self.name

