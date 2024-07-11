from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.


class AutoView(APIView):
    def get(self, request):
        cars = Auto.objects.all()
        serializer = AutoSerializer(cars, many=True)
        return Response(({'cars': serializer.data}))


    def post(self, request):
        car = request.data.get('cars')
        serializers = AutoSerializer(data=car)
        if serializers.is_valid(raise_exception=True):
            cars_saved = serializers.save()
            return Response({'ok': 'success'})


class CarPartViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = CarPart.objects.all()
        serializer = CarPartSerializer(queryset, many=True)
        return Response(serializer.data)


    def retrive(self, request, pk=None):
        queryset = CarPart.objects.all()
        car_parts = get_object_or_404(queryset, pk=pk)
        serializer = CarPartSerializer(car_parts)
        return Response(serializer.data)


class CountryView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CountrySerializer(queryset, many=True)
        return Response(serializer.data)
