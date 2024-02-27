from django.db import models

class Partner(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name = 'Название'
    )
    description = models.TextField(
        max_length=255,
        verbose_name = 'Описание'
    )
    photo = models.ImageField(
        verbose_name = 'Фото',
        null= True, blank=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
        