# Generated by Django 2.2.5 on 2019-09-21 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atc', '0005_auto_20190921_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atc',
            name='landings',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='atc',
            name='runways',
            field=models.PositiveSmallIntegerField(default=2),
        ),
    ]
