# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-20 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=200),
        ),
    ]
