# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 10:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annotations', '0004_auto_20171006_0013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='annotation',
            options={'ordering': ('number_of_recordings',)},
        ),
    ]
