#users/models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from PIL import Image
import os

class CustomUser(AbstractUser):
    usdt_balance = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)


    
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.png')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Обработка изображения
        img = Image.open(self.image.path)
        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)
