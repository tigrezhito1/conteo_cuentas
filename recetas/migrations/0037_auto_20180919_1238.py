# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-19 17:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0036_auto_20180919_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 19, 12, 38, 42, 180027), editable=False),
        ),
    ]
