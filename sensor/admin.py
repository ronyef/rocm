from django.contrib import admin
from .models import Machine, Compartment, Sensor, Value


admin.site.register(Machine)
admin.site.register(Compartment)
admin.site.register(Sensor)
admin.site.register(Value)
