# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-14 04:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rest', '0002_auto_20160814_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tienda',
            name='latitud',
            field=models.DecimalField(decimal_places=20, max_digits=20),
        ),
        migrations.AlterField(
            model_name='tienda',
            name='longitud',
            field=models.DecimalField(decimal_places=20, max_digits=20),
        ),
    ]
