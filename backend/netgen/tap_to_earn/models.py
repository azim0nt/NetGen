from django.db import models
from PIL import Image
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
    image = models.ImageField(upload_to='games-icon/',
                              default='games-icon/default.jpg')

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        
        # Создать путь для WebP-изображения
        webp_path = self.image.path.rsplit('.', 1)[0] + '.webp'
        
        # Сохранить изображение в формате WebP
        img.save(webp_path, 'WEBP')
        
        # Удалить оригинальный файл
        if os.path.exists(self.image.path):
            os.remove(self.image.path)
        
        # Обновить поле image для указания на новый WebP-файл
        self.image.name = self.image.name.rsplit('.', 1)[0] + '.webp'
        
        # Сохранить модель снова для обновления пути в базе данных
        super().save(update_fields=['image'])
