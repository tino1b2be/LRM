# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='code',
            field=models.CharField(default='xxx', max_length=10),
            preserve_default=False,
        ),
    ]
