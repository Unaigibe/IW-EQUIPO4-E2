# Generated by Django 3.0.4 on 2020-04-16 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDeustotilTECHSL', '0004_auto_20200416_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='foto_perfil',
            field=models.ImageField(blank=True, upload_to='fotos_perfil'),
        ),
    ]
