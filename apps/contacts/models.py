from django.db import models

class Contact(models.Model):
    first_name = models.CharField(
        max_length=255, 
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=255, 
        verbose_name='Фамилия'
    )
    phone = models.CharField(
        max_length=255, 
        verbose_name='Телефон'
    )
    email = models.EmailField(
        max_length=255, 
        verbose_name='Email'
    )
    message = models.TextField(
        max_length=255, 
        verbose_name='Сообщение'
    )

    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'