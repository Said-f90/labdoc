from django.db import models

class Team(models.Model):
    first_name = models.CharField(
        max_length=255, 
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=255, 
        verbose_name='Фамилия'
    )
    position = models.CharField(
        max_length=255, 
        verbose_name='Должность'
    )
    phone = models.CharField(
        max_length=255, 
        verbose_name='Телефон'
    )
    photo = models.ImageField(
        verbose_name='Фото',
        null= True, blank=True
    )

    def __str__(self) -> str:
        return self.first_name
    
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        
