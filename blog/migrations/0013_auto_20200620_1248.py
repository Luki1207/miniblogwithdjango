# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-20 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200620_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('value1', 'LPM'), ('value2', 'Ngadu Bako')], max_length=200),
        ),
    ]
