# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-18 19:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0021_auto_20180918_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 18, 19, 4, 44, 834673), editable=False),
        ),
    ]
