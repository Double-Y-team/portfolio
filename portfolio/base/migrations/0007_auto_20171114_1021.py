# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-13 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20171114_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
