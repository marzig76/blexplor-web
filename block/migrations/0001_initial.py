# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 15:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('magic_number', models.IntegerField()),
                ('block_size', models.IntegerField()),
                ('version', models.IntegerField()),
                ('prev_hash', models.CharField(max_length=100)),
                ('merkel_root', models.CharField(max_length=100)),
                ('block_time', models.IntegerField()),
                ('target', models.IntegerField()),
                ('nonce', models.IntegerField()),
                ('tx_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.IntegerField()),
                ('tx_input_count', models.IntegerField()),
                ('tx_output_count', models.IntegerField()),
                ('lock_time', models.IntegerField()),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='block.Block')),
            ],
        ),
        migrations.CreateModel(
            name='TxInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prev_hash', models.CharField(max_length=100)),
                ('index', models.IntegerField()),
                ('script_bytes', models.IntegerField()),
                ('sigscript', models.CharField(max_length=100)),
                ('sequence', models.IntegerField()),
                ('tx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='block.Tx')),
            ],
        ),
        migrations.CreateModel(
            name='TxOutput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('script_pk_bytes', models.IntegerField()),
                ('script_pk', models.CharField(max_length=100)),
                ('tx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='block.Tx')),
            ],
        ),
    ]
