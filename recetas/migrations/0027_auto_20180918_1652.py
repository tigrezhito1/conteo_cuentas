# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-18 21:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0026_auto_20180918_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 18, 16, 52, 25, 227565), editable=False),
        ),
        migrations.AlterField(
            model_name='datos',
            name='ticket',
            field=models.ImageField(default=1, upload_to='ticket'),
            preserve_default=False,
        ),
    ]
