# Generated by Django 5.0.7 on 2024-07-10 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='car_model',
            field=models.CharField(max_length=100, verbose_name='Модель автомобиля'),
        ),
    ]