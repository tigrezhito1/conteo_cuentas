# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-18 20:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0023_auto_20180918_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 18, 20, 58, 0, 205050), editable=False),
        ),
    ]
