from django.db import models

class Laborotory(models.Model):
    description = models.CharField(
        max_length=255,
        verbose_name='Описание'
    )
    plans = models.TextField(
        max_length=255,
        verbose_name='Планы'
    )
