# serializers.py
from rest_framework import serializers

from .models import Sensor

class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ('datetime', 'payload')
