# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-17 21:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0013_auto_20180917_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 17, 21, 43, 56, 237140), editable=False),
        ),
    ]