# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 04:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20170609_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]