# Generated by Django 2.0.2 on 2019-04-29 20:03

import Pag.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pag', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pag',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=Pag.models.image_Pag),
        ),
    ]