# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-17 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0005_auto_20160417_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='text',
            field=models.CharField(max_length=155, unique=True),
        ),
    ]