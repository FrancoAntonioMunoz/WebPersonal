# Generated by Django 2.0.2 on 2019-04-19 02:13

import Datos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre Personal')),
                ('descent', models.CharField(blank=True, max_length=240, null=True, verbose_name='Url')),
                ('image1', models.ImageField(upload_to=Datos.models.image_Datos1)),
                ('descent1', models.CharField(blank=True, max_length=240, null=True, verbose_name='Url')),
                ('image2', models.ImageField(upload_to=Datos.models.image_Datos2)),
                ('descent2', models.CharField(blank=True, max_length=240, null=True, verbose_name='Url')),
                ('image3', models.ImageField(upload_to=Datos.models.image_Datos3)),
                ('state', models.CharField(default='Activo', max_length=240)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha Actualización')),
            ],
            options={
                'verbose_name': 'Dato y rede social',
                'verbose_name_plural': 'Datos y redes sociales',
                'ordering': ['name'],
            },
        ),
    ]