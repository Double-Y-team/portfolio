# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-13 21:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typesofdishes',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
