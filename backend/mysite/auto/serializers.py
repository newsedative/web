from rest_framework import serializers

class AutoSerializer(serializers.Serializer):
    car_brand = serializers.CharField(max_length=100)
    car_model = serializers.CharField(max_length=100)