# Generated by Django 5.0.7 on 2024-07-09 19:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=100, verbose_name='Марка автомобиля')),
                ('country', models.TextField(max_length=100, verbose_name='Страна производства')),
                ('created_date', models.DateTimeField(default=datetime.datetime(2024, 7, 9, 19, 24, 0, 201979, tzinfo=datetime.timezone.utc), verbose_name='Дата создания записи')),
            ],
        ),
    ]