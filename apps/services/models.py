from django.db import models

class Service(models.Model):
    title = models.CharField(
        max_length=255, 
        verbose_name='Название'
    )
    description = models.TextField(
        max_length=255, 
        verbose_name='Описание'
    )
    photo = models.ImageField(
        verbose_name='Фото'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


