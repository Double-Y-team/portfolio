# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 01:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dishimg',
            name='is_main',
        ),
        migrations.AddField(
            model_name='dish',
            name='main_img',
            field=models.ImageField(blank=True, null=True, upload_to='base/dish_img/'),
        ),
    ]
