from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('machines', views.MachineView)
router.register('compartments', views.CompartmentView)
router.register('sensors', views.SensorView)
router.register('values', views.ValueView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/machines/<int:machine_id>/new_sensor', views.new_sensor, name="new_sensor"),
    path('dashboard/machines/<int:machine_id>', views.dashboard_sensors, name="sensors"),
    path('dashboard/sensors/<int:sensor_id>', views.sensor_values, name="values"),
    path('dashboard/new_machine/', views.new_machine, name='new_machine'),
]