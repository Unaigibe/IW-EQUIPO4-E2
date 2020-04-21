# Generated by Django 3.0.4 on 2020-04-21 08:44

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('appDeustotilTECHSL', '0012_auto_20200421_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_fin',
            field=models.DateField(default=datetime.datetime(2020, 4, 21, 8, 44, 33, 788387, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2020, 4, 21, 8, 44, 33, 788387, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='fecha_fin',
            field=models.DateField(default=datetime.datetime(2020, 4, 21, 8, 44, 33, 788387, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2020, 4, 21, 8, 44, 33, 788387, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='proyecto',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='appDeustotilTECHSL.Proyecto'),
        ),
    ]
