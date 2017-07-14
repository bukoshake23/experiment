# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 01:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20170607_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(max_length=25)),
                ('small_size', models.IntegerField(blank=True, null=True)),
                ('medium_size', models.IntegerField(blank=True, null=True)),
                ('large_size', models.IntegerField(blank=True, null=True)),
                ('no_size', models.IntegerField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.AddField(
            model_name='type',
            name='product_code',
            field=models.CharField(default=None, max_length=25),
        ),
    ]
