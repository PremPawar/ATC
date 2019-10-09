# Generated by Django 2.2.5 on 2019-09-21 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0004_auto_20190921_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='states',
            field=models.PositiveSmallIntegerField(choices=[(0, 'IDLE'), (1, 'TAKEOFF_DONE'), (2, 'IN_AIR'), (3, 'EMERGENCY'), (4, 'LANDING'), (5, 'LANDED')], default=0),
        ),
    ]
