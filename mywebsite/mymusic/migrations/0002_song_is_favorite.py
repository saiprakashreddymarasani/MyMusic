# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymusic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_favorite',
            field=models.BooleanField(default='False'),
        ),
    ]