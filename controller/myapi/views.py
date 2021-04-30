from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import SensorSerializer
from .models import Sensor


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
