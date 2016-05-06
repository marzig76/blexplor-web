# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-06 22:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0002_block_block_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='txinput',
            name='addr',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='txoutput',
            name='addr',
            field=models.CharField(default='', max_length=100),
        ),
    ]
