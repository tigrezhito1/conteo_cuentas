# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-26 16:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0042_auto_20180926_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 26, 11, 10, 21, 894161), editable=False),
        ),
    ]
