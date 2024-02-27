from django.db import models

class Job(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name = 'Название'
    )
    description = models.TextField(
        max_length=255,
        verbose_name = 'Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'
