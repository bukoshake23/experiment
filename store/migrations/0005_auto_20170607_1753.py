# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20170607_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='large_size',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='medium_size',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='no_size',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='small_size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]