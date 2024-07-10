from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.


class AutoView(APIView):
    def get(self, request):
        cars = Auto.objects.all()
        serializer = AutoSerializer(cars, many=True)
        return Response(({'car': serializer.data}))