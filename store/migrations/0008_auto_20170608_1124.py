# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 03:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20170608_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Order'),
        ),
        migrations.AlterField(
            model_name='type',
            name='product_code',
            field=models.CharField(max_length=25),
        ),
    ]
