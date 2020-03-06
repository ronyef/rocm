from rest_framework import serializers
from .models import Machine, Compartment, Sensor, Value


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ('url', 'id', 'name', 'make', 'site', 'user')


class CompartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Compartment
        fields = ('url', 'id', 'name')


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ('url', 'id', 'name', 'compartment', 'machine')


class ValueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Value
        fields = ('url', 'id', 'timestamp', 'viscosity', 'temperature', 'sensor')