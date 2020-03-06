from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from .models import Machine, Compartment, Sensor, Value
from .serializers import MachineSerializer, CompartmentSerializer, SensorSerializer, ValueSerializer


class MachineView(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer


class CompartmentView(viewsets.ModelViewSet):
    queryset = Compartment.objects.all()
    serializer_class = CompartmentSerializer
    permission_classes = (permissions.IsAdminUser,)


class SensorView(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class ValueView(viewsets.ModelViewSet):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer


def home(request):
    return render(request, 'sensor/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def logout_user(request):
    if request.POST:
        logout(request)
        return redirect('home')
    
    
def profile(request):
    return render(request, 'registration/profile.html')


@login_required
def dashboard(request):
    machines = Machine.objects.filter(user=request.user)

    return render(request, 'sensor/dashboard.html', {'machines': machines})


def dashboard_sensors(request, machine_id):
    sensors = Sensor.objects.filter(machine__id=machine_id)
    machines = Machine.objects.filter(user=request.user)
    selected_machine = Machine.objects.get(id=machine_id)
    return render(request, 'sensor/dashboard_sensors.html', {'machines': machines, 'sensors': sensors, 'selected_machine': selected_machine})


def sensor_values(request, sensor_id):
    machines = Machine.objects.filter(user=request.user)
    sensor = Sensor.objects.get(id=sensor_id)
    values = Value.objects.filter(sensor=sensor_id)
    return render(request, 'sensor/dashboard_values.html', {'machines': machines, 'sensor':sensor, 'values': values})


def new_machine(request):
    machines = Machine.objects.filter(user=request.user)

    class MachineForm(ModelForm):
        class Meta:
            model = Machine
            fields = ['name', 'make', 'site']

    if request.method == 'POST':
        form = MachineForm(request.POST)
        if form.is_valid():
            machine = form.save(commit=False)
            machine.user = request.user
            machine.save()
            return redirect('sensors', machine.id)
    else:
        form = MachineForm()
        return render(request, 'sensor/new_machine.html', {'machines': machines, 'form': form})


def new_sensor(request, machine_id):
    machines = Machine.objects.filter(user=request.user)
    mid = machine_id

    class SensorForm(ModelForm):
        class Meta:
            model = Sensor
            fields = ['name', 'compartment']

    if request.method == 'POST':
        form = SensorForm(request.POST)
        if form.is_valid():
            sensor = form.save(commit=False)
            sensor.machine_id = machine_id
            sensor.save()
            return redirect('values', sensor.id)
    else:
        form = SensorForm()
        return render(request, 'sensor/new_sensor.html', {'machines': machines, 'form': form, 'machine_id': mid})
