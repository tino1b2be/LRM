# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20171007_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
