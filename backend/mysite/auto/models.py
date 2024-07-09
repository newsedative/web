from django.db import models
from django.utils import timezone

# Create your models here.
class Auto(models.Model):
    car_brand = models.CharField(verbose_name='Марка автомобиля', max_length=100)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name='Страна производства', null=True)
    price = models.IntegerField(verbose_name='Стоимость', default=10)
    created_date = models.DateTimeField(verbose_name='Дата добавления записи', default=timezone.now)

    def __str__(self):
        return self.car_brand

class CarPart(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=200)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name='Страна производства', null=True)
    description = models.TextField(verbose_name='Описание', max_length=1000)
    autos = models.ManyToManyField('Auto', verbose_name='Подходит для автомобилей')

    def __str__(self):
        return self.name


class Country(models.Model):
    country_name = models.CharField(verbose_name='Название страны', max_length=100)
    code = models.CharField(verbose_name='Код страны', max_length=10, default='RUS')
    currency = models.CharField(verbose_name='Валюта', max_length=50, default='рубль')

    def __str__(self):
        return self.country_name