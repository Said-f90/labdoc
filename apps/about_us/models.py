from django.db import models

class About(models.Model):
    title = models.CharField(
        max_length=255, 
        verbose_name='О нас'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


