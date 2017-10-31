# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 18:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prompts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromptTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('verified', models.BooleanField(default=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Language')),
                ('original_prompt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prompts.Prompt')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
