from rest_framework import serializers
from .models import *


class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = ('car_brand', 'car_model', 'country', 'price', 'created_date')


class CarPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPart
        fields = ('name', 'country', 'description', 'autos')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('country_name', 'code', 'currency')