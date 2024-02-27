# Generated by Django 5.0.2 on 2024-02-16 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='contact',
            name='last_name',
            field=models.CharField(default=1, max_length=255, verbose_name='Фамилия'),
            preserve_default=False,
        ),
    ]
