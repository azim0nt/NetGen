from django.db import models
from PIL import Image
from colorthief import ColorThief
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
    image = models.ImageField(upload_to='games-icon/', default='games-icon/default.jpg')
    primary_color = models.CharField(max_length=7, blank=True, null=True)  # поле для хранения основного цвета

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Проверить, не используется ли изображение по умолчанию
        if self.image.name != 'games-icon/default.jpg':
            # Обработать изображение и сохранить его в формате WebP
            img = Image.open(self.image.path)
            webp_path = self.image.path.rsplit('.', 1)[0] + '.webp'
            img.save(webp_path, 'WEBP')

            # Удалить оригинальное изображение
            if os.path.exists(self.image.path):
                os.remove(self.image.path)

            # Обновить путь к изображению на новый формат
            self.image.name = self.image.name.rsplit('.', 1)[0] + '.webp'

            # Извлечь основной цвет изображения
            color_thief = ColorThief(webp_path)
            dominant_color = color_thief.get_color(quality=1)
            # Преобразовать цвет в формат HEX
            self.primary_color = '#{:02x}{:02x}{:02x}'.format(dominant_color[0], dominant_color[1], dominant_color[2])

            # Сохранить модель снова для обновления пути в базе данных и основного цвета
            super().save(update_fields=['image', 'primary_color'])
