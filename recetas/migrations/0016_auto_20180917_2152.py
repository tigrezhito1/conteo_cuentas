# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-17 21:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0015_auto_20180917_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 17, 21, 52, 7, 400073), editable=False),
        ),
    ]
