# Generated by Django 2.2.5 on 2019-09-21 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atc', '0003_auto_20190921_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='atc',
            name='landings',
            field=models.PositiveSmallIntegerField(default=2),
        ),
        migrations.AddField(
            model_name='atc',
            name='takeoffs',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]