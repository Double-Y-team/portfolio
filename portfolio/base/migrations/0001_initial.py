# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 23:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='max_length=256', max_length=256)),
                ('description', models.CharField(help_text='max_length=256', max_length=256)),
                ('img', models.ImageField(upload_to='base/countries/img/')),
                ('flag', models.ImageField(upload_to='base/countries/flag/')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='max_length=256', max_length=256)),
                ('description', models.CharField(blank=True, help_text='max_length=256', max_length=256)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Countries')),
            ],
            options={
                'verbose_name': 'National Dish',
                'verbose_name_plural': 'National Dishes',
            },
        ),
        migrations.CreateModel(
            name='DishImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='name of picture (name_"img")', max_length=256)),
                ('img', models.ImageField(upload_to='base/dish_img/')),
                ('is_activ', models.BooleanField(default=False)),
                ('is_main', models.BooleanField(default=True)),
                ('upload', models.DateTimeField(auto_now_add=True)),
                ('dish', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Dish')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
    ]
