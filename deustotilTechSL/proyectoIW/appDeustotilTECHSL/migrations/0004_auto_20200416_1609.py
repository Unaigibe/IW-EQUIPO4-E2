# Generated by Django 3.0.4 on 2020-04-16 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDeustotilTECHSL', '0003_auto_20200416_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='foto_perfil',
            field=models.ImageField(upload_to='fotos_perfil'),
        ),
    ]
