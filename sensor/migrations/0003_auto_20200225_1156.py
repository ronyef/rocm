# Generated by Django 3.0.2 on 2020-02-25 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0002_machine_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compartment',
            name='machine',
        ),
        migrations.AddField(
            model_name='sensor',
            name='machine',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sensor.Machine'),
            preserve_default=False,
        ),
    ]
