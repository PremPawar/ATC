# Generated by Django 2.2.5 on 2019-09-21 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('atc', '0004_auto_20190921_2228'),
        ('flight', '0005_flight_states'),
    ]

    operations = [
        migrations.CreateModel(
            name='Takeoff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flight_takingoff', to='flight.Flight')),
                ('runway', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tekeoff_runway', to='atc.Runway')),
            ],
        ),
        migrations.CreateModel(
            name='Landing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flight_landing', to='flight.Flight')),
                ('runway', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='landing_runway', to='atc.Runway')),
            ],
        ),
    ]