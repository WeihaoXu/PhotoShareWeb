# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-20 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0006_auto_20170820_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(blank=True, max_length=254),
        ),
    ]
