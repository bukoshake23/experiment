# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_order_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='large_size',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='medium_size',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='small_size',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='large_size',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='medium_size',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='no_size',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='small_size',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
