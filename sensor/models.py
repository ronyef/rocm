from django.db import models
from django.contrib.auth.models import User


class Machine(models.Model):
    name = models.CharField(max_length=100)
    make = models.CharField(max_length=100, blank=True)
    site = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Compartment(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    compartment = models.ForeignKey(Compartment, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Value(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    viscosity = models.FloatField()
    temperature = models.FloatField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)

    def __str__(self):
        return self.sensor.name
